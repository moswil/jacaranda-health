import enum
from os import name

from sqlalchemy import Enum

from . import db
from .base_model import BaseModel


class MessageType(enum.Enum):
    INCOMING = 'INCOMING'
    OUTGOING = 'OUTGOING'


class Message(BaseModel):
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
    user_id = db.Column(db.Integer(), nullable=False)

    ticket_id = db.Column(db.Integer, db.ForeignKey(
        'tickets.ticket_id'), nullable=False)

    def __init__(self, id, description, message_type, created, updated, user_id, ticket_id) -> None:
        self.id = id
        self.description = description
        self.message_type = message_type
        self.created = created
        self.updated = updated
        self.user_id = user_id
        self.ticket_id = ticket_id

    def __repr__(self) -> str:
        return (
            f"**Message** "
            f"message_id: {self.id} "
            f"description: {self.description} "
            f"message_type: {self.message_type}"
            f"user_id: {self.user_id}"
            f"**Message** "
        )
