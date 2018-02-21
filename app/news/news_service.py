from .news_repository import get_all


def index():
    res = get_all()
    return res
