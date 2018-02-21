from .news_model import News
from helpers.database import db


class NewsRepository:
    soft_delete = True

    def __init__(self, **kwargs):
        self.doc = News(**kwargs)

    def save(self):
        db.session.add(self.doc)
        db.session.commit()
        return self.doc
