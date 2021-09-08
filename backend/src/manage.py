from flask.cli import FlaskGroup

from app import app
from app.services.save_to_db import seed_data


cli = FlaskGroup(app)


@cli.command()
def seed():
    """Seeds data from CSV to tables.
    """
    seed_data()


if __name__ == '__main__':
    cli()
