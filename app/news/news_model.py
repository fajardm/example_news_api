import enum
from datetime import datetime
from helpers.database import db


class Status(enum.Enum):
    draft = 'draft'
    publish = 'publish'


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    status = db.Column(db.Enum(Status), nullable=False, default=Status.draft)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)
