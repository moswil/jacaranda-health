import pandas as pd
import os

from app.utils.logger import get_logger

from .messages_data import messages_df
from .subjects_data import df_ticket_sbj_phone

LOGGER = get_logger()

merged_df = pd.merge(df_ticket_sbj_phone, messages_df, on=['ticket_id'])


tickets_data = merged_df[['ticket_id', 'phone_number', 'sbj', 'intents']]
messages_data = merged_df[['ticket_id',
                           'incoming_messages', 'outgoing_messages']]
incoming_messages = merged_df[['ticket_id', 'incoming_messages']]
outgoing_messages = merged_df[['ticket_id', 'outgoing_messages']]


def run() -> bool:
    try:
        current_path = os.path.dirname(os.path.abspath(__file__))
        resources_path = os.path.join(current_path, 'resources')
        tickets_data.to_csv(os.path.join(
            resources_path, 'tickets_data.csv'), index=False)
        messages_data.to_csv(os.path.join(
            resources_path, 'messages_data.csv'), index=False)
        incoming_messages.to_csv(
            os.path.join(
                resources_path, 'incoming_messages.csv'), index=False)
        outgoing_messages.to_csv(
            os.path.join(
                resources_path, 'outgoing_messages.csv'), index=False)
        return True
    except Exception as e:
        LOGGER.error(f'EXCEPTION: {e} occurred')
        return False
