from wtforms import Form, StringField, validators, Field


class TagListField(Field):
    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist
        else:
            self.data = []


class CreateNewsForm(Form):
    title = StringField('Title', [validators.DataRequired()])
    description = StringField('Description', [validators.DataRequired()])
    status = StringField('Status')
    topics = TagListField('Topics')
