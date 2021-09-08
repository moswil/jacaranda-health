from marshmallow_enum import EnumField

from . import ma
from app.models.message import Message, MessageType


class MessageSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Message
        load_instance = True
        # load_only = ("id",)
        include_fk = True

    message_type = EnumField(MessageType, by_value=True)
