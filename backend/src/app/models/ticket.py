from sqlalchemy.dialects.postgresql import ARRAY

from app import db


class Ticket(db.Model):

    __tablename__ = 'tickets'

    ticket_id = db.Column(db.Integer(), primary_key=True)
    subject = db.Column(db.String(300), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    intents = db.Column(db.String(20))

    incoming_message = db.relationships(
        'Message', backref='ticket', lazy=True)
    outgoing_message = db.relationships(
        'Message', backref='ticket', lazy=True)

    def __repr__(self) -> str:
        return (
            f"**Ticket** "
            f"ticket_id: {self.ticket_id} "
            f"subject: {self.subject} "
            f"phone: {self.phone}"
            f"intents: {self.intents}"
            f"**Ticket** "
        )
