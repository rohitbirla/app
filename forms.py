from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField


class AddForm(FlaskForm):
    name  = StringField('NAme of the Puppy:')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):
    id = IntegerField("Id Number of the Puppy to Remove: ")
    submit = SubmitField("Remove Puppy")