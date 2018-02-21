from datetime import datetime
from helpers.database import db
from helpers.marshmallow import ma


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    status = db.Column(db.Enum('draft', 'publish'), nullable=False, default='draft')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)


class NewsSchema(ma.ModelSchema):
    class Meta:
        model = News
