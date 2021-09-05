from app import db
from app.models.message import Message


class MessageRepository:

    @staticmethod
    def get_message_by_id(id):
        return db.session.query(Message).get(id)

    @staticmethod
    def get_all_messages():
        return db.session.query(Message).all()
