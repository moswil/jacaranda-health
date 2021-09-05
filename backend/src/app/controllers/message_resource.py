from flask_restx import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from app import api
from app.repositories.message_repository import MessageRepository
from app.utils.logger import get_logger

MESSAGES_ENDPOINT = '/api/messages'
LOGGER = get_logger()

ns = api.namespace('messages', description="Messages CRUD")


@ns.route(MESSAGES_ENDPOINT)
class MessageResource(Resource):

    def get(self, id=None):
        if not id:
            LOGGER.info("Retrieving all messages...")
            return MessageRepository.get_all_messages(), 200
        try:
            return MessageRepository.get_message_by_id(id)
        except NoResultFound:
            LOGGER.error(f'Message with id: {id} NOT found.')
            abort(404, "Message not found")
