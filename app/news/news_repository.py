from .news_model import News
from helpers.database import db


def get_all():
    res = News.query.all()
    return res


def create(commit=True, **kwargs):
    doc = News(**kwargs)
    res = db.session.add(doc)
    if commit:
        res = db.session.commit()
    return doc, res
