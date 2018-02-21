from .news_repository import NewsRepository


def news_list(**criteria):
    if criteria['status']:
        if criteria['status'] == 'deleted':
            return NewsRepository.get_all(deleted_at=not None).get_doc()
        else:
            return NewsRepository.get_all(status=criteria['status']).get_doc()

    return NewsRepository.get_all().get_doc()


def create_news(**data):
    doc = NewsRepository(
        title=data['title'],
        description=data['description'],
        status=data['status'] if data['status'] else 'draft'
    ).save().get_doc()
    return doc


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
