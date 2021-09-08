import os


from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_restx import Api
from marshmallow import ValidationError

from .models import db
from .schema import ma
from .utils.logger import get_logger

LOGGER = get_logger()


app = Flask(__name__)
rest_api = Api(app, version='0.0.1', title='Ticketing API',
               description='A simple ticketing API',)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')

LOGGER.info(f'DB_URL: {os.getenv("DATABASE_URL")}')

#
db.init_app(app)


@rest_api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


# add routes
from . import routes  # noqa

ma.init_app(app)
migrate = Migrate(app, db)


# add models to enable migrations
from app.models.message import Message  # noqa
from app.models.ticket import Ticket  # noqa
