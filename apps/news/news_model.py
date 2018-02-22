from helpers.database import db
from helpers.base_model import BaseModel
from apps.topics.topics_model import Topics

news_topics = db.Table('news_topics',
                       db.Column('news_id', db.Integer, db.ForeignKey('news.id', ondelete='CASCADE'), primary_key=True),
                       db.Column('topics_id', db.Integer, db.ForeignKey('topics.id', ondelete='CASCADE'),
                                 primary_key=True)
                       )


class News(BaseModel):
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    status = db.Column(db.Enum('draft', 'publish'), nullable=False, default='draft')
    topics = db.relationship(Topics, secondary=news_topics, lazy='subquery', backref=db.backref('news_id', lazy=True),
                             cascade="all,delete")
