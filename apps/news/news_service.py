from .news_repository import NewsRepository, News
from apps.topics.topics_repository import TopicsRepository


def news_list(**criteria):
    if criteria['status']:
        if criteria['status'] == 'deleted':
            return NewsRepository.query().filter(News.deleted_at.isnot(None)).all()
        else:
            return NewsRepository.query().filter(News.status == criteria['status']).all()

    return NewsRepository.query().filter(News.deleted_at.is_(None)).all()


def create_news(**data):
    repo = NewsRepository(
        title=data['title'],
        description=data['description'],
        status=data['status'] if data['status'] else 'draft'
    )

    if data['topics']:
        for item in data['topics']:
            topic = TopicsRepository.get_by_id(item).get_doc()
            if topic:
                repo.get_doc().topics.append(topic)

    repo.save()

    return repo.get_doc()


def show_news(id):
    repo = NewsRepository.get_by_id(id)
    return repo.get_doc()


def update_news(id, **data):
    repo = NewsRepository.get_by_id(id)

    if repo.get_doc():
        repo.get_doc().title = data['title']
        repo.get_doc().description = data['description']
        repo.get_doc().status = data['status'] if data['status'] else doc.status
        repo.save()

    return repo.get_doc()


def destroy_news(id):
    repo = NewsRepository.destroy_by_id(id)
    return repo.get_doc()
