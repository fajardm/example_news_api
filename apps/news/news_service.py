from .news_repository import NewsRepository, News
from apps.topics.topics_repository import TopicsRepository, Topics


def news_list(**criteria):
    temp_query = NewsRepository.query()
    if criteria['status']:
        if criteria['status'] == 'deleted':
            temp_query = temp_query.filter(News.deleted_at.isnot(None))
        else:
            temp_query = temp_query.filter(News.status == criteria['status'])

    if criteria['topics']:
        temp_query = temp_query.filter(News.topics.any(Topics.name.in_(criteria['topics'])))

    return temp_query.all()


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
        repo.get_doc().status = data['status'] if data['status'] else repo.get_doc().status

        for topic in repo.get_doc().topics:
            if topic.id not in data['topics']:
                repo.get_doc().topics.remove(topic)

        if data['topics']:
            for item in data['topics']:
                topic = TopicsRepository.get_by_id(item).get_doc()
                if topic:
                    repo.get_doc().topics.append(topic)

        repo.save()

    return repo.get_doc()


def destroy_news(id):
    repo = NewsRepository.destroy_by_id(id)
    return repo.get_doc()
