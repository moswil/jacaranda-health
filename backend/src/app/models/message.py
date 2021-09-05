import enum

from app import db

from sqlalchemy import Enum


class MessageType(enum.Enum):
    INCOMING = 'INCOMING'
    OUTGOING = 'OUTGOING'


class Message(db.Model):
    """Represents the Message model.

    Args:
        db ([type]): [description]
    """

    __tablename__ = 'messages'

    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(256), nullable=False)
    message_type = db.Column(Enum(MessageType))
    created = db.Column(db.DateTime(), nullable=False)
    updated = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer())

    ticket_id = db.Column(db.Integer, db.ForeignKey(
        'ticket.ticket_id'), nullable=False)

    def __repr__(self) -> str:
        return (
            f"**Message** "
            f"message_id: {self.id} "
            f"description: {self.description} "
            f"message_type: {self.message_type}"
            f"user_id: {self.user_id}"
            f"**Message** "
        )
