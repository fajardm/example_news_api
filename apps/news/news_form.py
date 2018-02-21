from wtforms import Form, StringField, validators


class CreateNewsForm(Form):
    title = StringField('Title', [validators.DataRequired()])
    description = StringField('Description', [validators.DataRequired()])
    status = StringField('Status')
