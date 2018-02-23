from helpers.marshmallow import ma
from .topics_model import Topics


class TopicsSchema(ma.ModelSchema):
    class Meta:
        model = Topics
