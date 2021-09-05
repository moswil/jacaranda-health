from app import db
from app.models.ticket import Ticket


class TicketRepository:

    @staticmethod
    def get_ticket_by_id(id):
        return db.session.query(Ticket).get(id)

    @staticmethod
    def get_all_tickets():
        return db.session.query(Ticket).all()
