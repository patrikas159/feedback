from wtforms import StringField, TextAreaField, SelectField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from .category import categories
from .ivertinimas import ivertinimas


class FeedbackForm(FlaskForm):

    name = StringField("Title:",validators=[InputRequired()])
    category = SelectField('Category', choices=categories.values())
    ivertinimas = SelectField('Rating', choices=ivertinimas.values())
    code = IntegerField('Code')
    description = TextAreaField("Description", validators=[InputRequired()])