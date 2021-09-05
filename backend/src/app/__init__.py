import os


from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from app.utils.logger import get_logger

LOGGER = get_logger()


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')

LOGGER.info(f'DB_URL: {os.getenv("DATABASE_URL")}')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

from app.models.message import Message  # noqa
from app.models.ticket import Ticket  # noqa
