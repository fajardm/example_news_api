from .news_model import News


def news_list(**criteria):
    doc = News.query
    if criteria['status']:
        if criteria['status'] == 'deleted':
            doc = doc.filter(News.deleted_at.isnot(None))
        else:
            doc = doc.filter(News.status == criteria['status'])

    doc = doc.all()

    return doc
