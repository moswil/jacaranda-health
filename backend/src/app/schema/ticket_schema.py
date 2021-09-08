from marshmallow import fields
from sqlalchemy.orm import load_only

from . import ma
from app.models.ticket import Ticket
from app.schema.message_schema import MessageSchema


class TicketSchema(ma.SQLAlchemyAutoSchema):

    messages = ma.Nested(MessageSchema, many=True)

    class Meta:
        model = Ticket
        load_instance = True
        # load_only = ('ticket_id',)
        ordered = True

    incoming_message = fields.Nested(MessageSchema, many=True)
    outgoing_message = fields.Nested(MessageSchema, many=True)
