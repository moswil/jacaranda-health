from marshmallow import fields

from app import ma
from app.models.ticket import Ticket
from app.schema.message_schema import MessageSchema


class TicketSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Ticket

    incoming_message = fields.Nested(MessageSchema, many=True)
    outgoing_message = fields.Nested(MessageSchema, many=True)
