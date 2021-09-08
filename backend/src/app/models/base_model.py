from . import db


class BaseModel(db.Model):

    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    # TODO: should not delete from the database
    def delete(self):
        db.session.delete(self)
        db.session.commit()
