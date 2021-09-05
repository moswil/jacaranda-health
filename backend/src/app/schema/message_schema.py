from marshmallow_enum import EnumField

from app import ma
from app.models.message import Message, MessageType


class MessageSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Message

    message_type = EnumField(MessageType, by_value=True)
