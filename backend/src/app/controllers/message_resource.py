from flask import request
from flask_restx import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from app.models import db
from app.repositories.message_repository import MessageRepository
from app.utils.logger import get_logger

from app.schema.message_schema import MessageSchema


LOGGER = get_logger()
MESSAGE_NOT_FOUND = "Message not found"
MESSAGE_WITH_ID_NOT_FOUND = 'Message with id: {} NOT found.'

message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)


class MessageResource(Resource):

    def get(self, id):
        try:
            message = MessageRepository.get_message_by_id(id)
            if message:
                return message_schema.dump(message)
        except NoResultFound:
            LOGGER.error(MESSAGE_WITH_ID_NOT_FOUND.format(id))
            abort(404, MESSAGE_NOT_FOUND)

    def delete(self, id):
        try:
            message = MessageRepository.get_message_by_id(id)
            if message:
                LOGGER.warn(f'DELETING messages: {message}')
                message.delete()
                return [], 204
            else:
                return MESSAGE_NOT_FOUND, 404
        except NoResultFound:
            LOGGER.error(MESSAGE_WITH_ID_NOT_FOUND.format(id))
            abort(404, MESSAGE_NOT_FOUND)

    def put(self, id):
        try:
            message = MessageRepository.get_message_by_id(id)
            message_json = request.get_json()

            if message:
                LOGGER.warn(f'UPDATING message: {message}')
                message.description = message_json['description']

                message.save()

                return message_schema.dump(message), 200
            else:
                return MESSAGE_NOT_FOUND, 404
        except NoResultFound:
            LOGGER.error(MESSAGE_WITH_ID_NOT_FOUND.format(id))
            abort(404, MESSAGE_NOT_FOUND)


class MessagesResource(Resource):

    def get(self):
        """Lists all messages.

        Returns:
            [type]: [description]
        """
        try:
            LOGGER.info("Retrieving all messages...")
            messages = MessageRepository.get_all_messages()
            return messages_schema.dump(messages), 200
        except NoResultFound:
            LOGGER.error(MESSAGE_WITH_ID_NOT_FOUND.format(id))
            abort(404, MESSAGE_NOT_FOUND)

    def post(self):
        message_json = request.get_json()

        LOGGER.info(f'Messages JSON: {message_json}')

        message_data = message_schema.load(message_json, session=db.session)
        message_data.save()

        return message_schema.dump(message_data), 201
