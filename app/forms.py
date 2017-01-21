from wtforms import Form, StringField


class NameForm(Form):
    name = StringField('Name')
