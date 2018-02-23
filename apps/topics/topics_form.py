from wtforms import Form, StringField, validators, ValidationError
from .topics_repository import TopicsRepository


class CreateTopicForm(Form):
    name = StringField('Name', [validators.DataRequired()])

    def validate_name(form, field):
        doc = TopicsRepository.get_by_id(field.data).get_doc()
        if doc:
            raise ValidationError('Name must be unique')
