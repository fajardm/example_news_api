from wtforms import Form, StringField, validators


class CreateTopicForm(Form):
    name = StringField('Name', [validators.DataRequired()])
