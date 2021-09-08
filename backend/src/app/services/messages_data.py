import pandas as pd
import os

from datetime import datetime
from typing import Any, Dict, Tuple

from .utils import read_excel_data


def get_intent_and_description(body_text: str) -> Tuple[str, str]:
    intent = ''
    description = ''
    if 'intent' in body_text:
        intent = body_text.split(' ')[2]
        description = ' '.join(body_text.split(' ')[5:])
    else:
        intent = None
        description = body_text
    return intent, description


def create_message_object(msg_id: int, msg: str, user_id: int, created: datetime) -> Dict[str, Any]:
    return {
        "id": int(msg_id),
        "message": msg,
        "created": created,
        "updated": created,
        "user_id": int(user_id)
    }


def group_message_df(groupby_obj):

    messages_df_list = []

    for group_name, df_group in groupby_obj:
        incoming_message = []
        outgoing_message = []
        intents = set()
        for _, row in df_group.iterrows():

            if row['incoming'] == True:
                incoming_message.append(row['message'])
                intents.add(row['intent'])
            else:
                outgoing_message.append(row['message'])
                intents.add(row['intent'])

        messages_df_list.append(
            [group_name, list(intents), incoming_message, outgoing_message])

    return messages_df_list


current_path = os.path.dirname(os.path.abspath(__file__))
resources_path = os.path.join(current_path, 'resources')

df_messages = read_excel_data(os.path.join(resources_path,
                                           'Software_Developer_Interview_Assignment.xlsx'), sheet_name='Messages')

df_messages['intent'] = df_messages.apply(
    lambda row: get_intent_and_description(row['body_text'])[0], axis=1)

df_messages['description'] = df_messages.apply(
    lambda row: get_intent_and_description(row['body_text'])[1], axis=1)

df_messages['message'] = df_messages.apply(lambda row: create_message_object(
    row['id'], row['description'], row['user_id'], row['created_at']), axis=1)

# groupby
obj = df_messages.groupby('ticket_id')

messages_df_list = group_message_df(obj)

messages_df = pd.DataFrame(messages_df_list, columns=[
                           'ticket_id', 'intents', 'incoming_messages', 'outgoing_messages'])
