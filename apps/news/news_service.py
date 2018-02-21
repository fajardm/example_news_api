from .news_model import News
from helpers.database import db


def news_list(**criteria):
    doc = News.query
    if criteria['status']:
        if criteria['status'] == 'deleted':
            doc = doc.filter(News.deleted_at.isnot(None))
        else:
            doc = doc.filter(News.status == criteria['status'])

    doc = doc.all()

    return doc


def create_news(**data):
    doc = News(
        title=data['title'],
        description=data['description'],
        status=data['status'] if data['status'] else 'draft'
    )
    db.session.add(doc)
    db.session.commit()
    return doc


def show_news(id):
    doc = News.query.get(id)
    return doc


def update_news(id, **data):
    doc = News.query.get(id)

    if doc:
        doc.title = data['title']
        doc.description = data['description']
        doc.status = data['status'] if data['status'] else doc.status

        db.session.add(doc)
        db.session.commit()

    return doc


def destroy_news(id):
    doc = News.query.get(id)

    if doc:
        db.session.delete(doc)
        db.session.commit()

    return doc
