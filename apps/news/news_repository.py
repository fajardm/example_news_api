from .news_model import News
from datetime import datetime
from helpers.database import db


class NewsRepository:
    soft_delete = True

    def __init__(self, **kwargs):
        self._doc = News(**kwargs)

    def save(self):
        db.session.add(self._doc)
        db.session.commit()
        return self

    def get_doc(self):
        return self._doc

    @classmethod
    def get_all(cls, **criterion):
        obj = cls()
        obj._doc = News.query.filter_by(**criterion).all()
        return obj

    @classmethod
    def get_by_id(cls, id):
        obj = cls()

        temp_query = News.query

        if obj.soft_delete:
            temp_query = temp_query.filter_by(deleted_at=None)

        temp_query = temp_query.filter_by(id=id).first()

        obj._doc = temp_query

        return obj

    @classmethod
    def destroy_by_id(cls, id):
        res = NewsRepository.get_by_id(id)

        if res.get_doc():
            res.get_doc().deleted_at = datetime.utcnow()
            res.save()

        return res
