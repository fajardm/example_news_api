from wtforms import Form, StringField, validators, ValidationError
from .topics_repository import TopicsRepository


class CreateTopicForm(Form):
    name = StringField('Name', [validators.DataRequired()])

    def validate_name(form, field):
        doc = TopicsRepository.query().filter_by(name=field.data).first()
        if doc:
            raise ValidationError('Name must be unique')
