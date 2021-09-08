from app import rest_api

from .controllers.tickets_resource import TicketResource, TicketsResource
from .controllers.message_resource import MessageResource, MessagesResource

rest_api.add_resource(MessagesResource, '/api/v1/messages/')
rest_api.add_resource(MessageResource, '/api/v1/messages/<int:id>')
rest_api.add_resource(TicketsResource, '/api/v1/tickets/')
rest_api.add_resource(TicketResource, '/api/v1/tickets/<int:id>')
