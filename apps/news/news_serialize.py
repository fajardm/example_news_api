from helpers.marshmallow import ma
from .news_model import News


class NewsSchema(ma.ModelSchema):
    class Meta:
        model = News
