import pandas as pd
import os

from typing import List

from app.models.ticket import Ticket
from app.utils.logger import get_logger

from .combined_df import run


LOGGER = get_logger()


def save_to_tickets_table(ticket_id: int, phone: str, subject: str, intents):
    # save
    intents = intents[1:-1]
    intents = intents.split(',')
    if 'None' in intents:
        intents.remove('None')
    ticket = Ticket(int(ticket_id), str(phone), subject, intents)
    # call ticket.save() -> to save the model
    ticket.save()


def seed_data():

    # invoke run
    result = run()

    LOGGER.debug(f'Value of result: {result}')

    if result:
        LOGGER.info('Seeding data')
        current_path = os.path.dirname(os.path.abspath(__file__))
        resources_path = os.path.join(current_path, 'resources')
        tickets_data = pd.read_csv(os.path.join(
            resources_path, 'tickets_data.csv'))
        incoming_messages = pd.read_csv(os.path.join(
            resources_path, 'incoming_messages.csv'))
        outgoing_messages = pd.read_csv(os.path.join(
            resources_path, 'outgoing_messages.csv'))

        # apply the data and save to db
        tickets_data.apply(lambda row: save_to_tickets_table(
            row['ticket_id'], row['phone_number'], row['sbj'], row['intents']), axis=1)
    else:
        LOGGER.warn('FAILED to Seed data...')
