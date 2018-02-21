import enum

from helpers.database import db


class Status(enum.Enum):
    draft = 'draft'
    publish = 'publish'


class News(db.Model):
    title = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    status = db.Column(db.Enum(Status))
