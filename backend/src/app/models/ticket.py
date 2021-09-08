from sqlalchemy.dialects.postgresql import ARRAY

from . import db
from .base_model import BaseModel


class Ticket(BaseModel):

    __tablename__ = 'tickets'

    ticket_id = db.Column(db.Integer(), primary_key=True)
    phone = db.Column(db.String(20), nullable=True)
    subject = db.Column(db.String(300), nullable=True)
    intents = db.Column(ARRAY(db.String(20)))

    messages = db.relationship('Message', backref='tickets', lazy='dynamic')

    # incoming_messages = db.relationship(
    #     'Message', primaryjoin='Ticket.ticket_id == Message.ticket_id', backref='incoming', lazy='dynamic')
    # outgoing_messages = db.relationship(
    #     'Message', primaryjoin='Ticket.ticket_id == Message.ticket_id', backref='outgoing', lazy='dynamic')

    def __init__(self, ticket_id, phone, subject, intents) -> None:
        self.ticket_id = ticket_id
        self.phone = phone
        self.subject = subject
        self.intents = intents

    def __repr__(self) -> str:
        return (
            f"**Ticket** "
            f"ticket_id: {self.ticket_id} "
            f"subject: {self.subject} "
            f"phone: {self.phone}"
            f"intents: {self.intents}"
            f"**Ticket** "
        )
