from .topics_model import Topics
from datetime import datetime
from helpers.database import db


class TopicsRepository:
    soft_delete = True

    def __init__(self, **kwargs):
        self._doc = Topics(**kwargs)

    def save(self):
        db.session.add(self._doc)
        db.session.commit()
        return self

    def get_doc(self):
        return self._doc

    @classmethod
    def query(cls):
        return Topics.query.filter_by(deleted_at=None)

    @classmethod
    def get_by_id(cls, id):
        obj = cls()

        temp_query = Topics.query

        if obj.soft_delete:
            temp_query = temp_query.filter_by(deleted_at=None)

        temp_query = temp_query.filter_by(id=id).first()

        obj._doc = temp_query

        return obj

    @classmethod
    def destroy_by_id(cls, id):
        res = TopicsRepository.get_by_id(id)

        if res.get_doc():
            res.get_doc().deleted_at = datetime.utcnow()
            db.engine.execute("DELETE FROM news_topics WHERE topics_id = " + id)
            res.save()

        return res
