from .topics_repository import TopicsRepository


def topics_list():
    doc = TopicsRepository.query().all()
    return doc


def create_topic(**data):
    doc = TopicsRepository(name=data['name']).save().get_doc()
    return doc


def show_topic(id):
    repo = TopicsRepository.get_by_id(id)
    return repo.get_doc()


def update_topic(id, **data):
    repo = TopicsRepository.get_by_id(id)

    if repo.get_doc():
        repo.get_doc().name = data['name']
        repo.save()

    return repo.get_doc()


def destroy_topic(id):
    repo = TopicsRepository.destroy_by_id(id)
    return repo.get_doc()
