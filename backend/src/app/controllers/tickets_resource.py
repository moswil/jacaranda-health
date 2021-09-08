from app.core.exceptions import DuplicateTicket
from flask import request
from flask_restx import Resource, abort
from sqlalchemy.orm.exc import NoResultFound


from app.models import db
from app.repositories.ticket_repository import TicketRepository
from app.schema.ticket_schema import TicketSchema
from app.utils.logger import get_logger


LOGGER = get_logger()
TICKET_NOT_FOUND = "Ticket not found"
TICKET_WITH_ID_NOT_FOUND = 'Ticket with id: {} NOT found.'

ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)


class TicketResource(Resource):
    def get(self, id):
        """List a ticket with a given ticket.

        Returns:
            [type]: [description]
        """
        try:
            ticket = TicketRepository.get_ticket_by_id(id)
            if ticket:
                return ticket_schema.dump(ticket)
            else:
                return TICKET_NOT_FOUND, 404
        except NoResultFound:
            LOGGER.error(TICKET_WITH_ID_NOT_FOUND.format(id))
            abort(404, TICKET_NOT_FOUND)

    def delete(self, id):
        try:
            ticket = TicketRepository.get_ticket_by_id(id)
            if ticket:
                LOGGER.warn(f'DELETING ticket: {ticket}')
                ticket.delete()
                return [], 204
            else:
                return TICKET_NOT_FOUND, 404
        except NoResultFound:
            LOGGER.error(TICKET_WITH_ID_NOT_FOUND.format(id))
            abort(404, TICKET_NOT_FOUND)

    def put(self, id):
        try:
            ticket = TicketRepository.get_ticket_by_id(id)
            ticket_json = request.get_json()

            if ticket:
                LOGGER.warn(f'UPDATING ticket: {ticket}')
                ticket.subject = ticket_json['subject']
                ticket.phone = ticket_json['phone']
                ticket.intents = ticket_json['intents']

                ticket.save()

                return ticket_schema.dump(ticket), 200
            else:
                return TICKET_NOT_FOUND, 404
        except NoResultFound:
            LOGGER.error(TICKET_WITH_ID_NOT_FOUND.format(id))
            abort(404, TICKET_NOT_FOUND)


class TicketsResource(Resource):
    def get(self):
        """Lists all tickets.

        Returns:
            [type]: [description]
        """
        try:
            LOGGER.info("Retrieving all tickets...")
            tickets = TicketRepository.get_all_tickets()
            return tickets_schema.dump(tickets), 200
        except NoResultFound:
            LOGGER.error(TICKET_WITH_ID_NOT_FOUND.format(id))
            abort(404, TICKET_NOT_FOUND)

    def post(self):
        ticket_json = request.get_json()

        LOGGER.info(f'Tickets JSON: {ticket_json}')

        ticket_id = ticket_json['ticket_id']
        is_ticket_id_present = TicketRepository.get_ticket_by_id(ticket_id)

        if is_ticket_id_present:
            raise DuplicateTicket('Ticket already exists')

        ticket_data = ticket_schema.load(ticket_json, session=db.session)
        ticket_data.save()

        return ticket_schema.dump(ticket_data), 201
