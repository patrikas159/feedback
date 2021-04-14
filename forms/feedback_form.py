from wtforms import StringField, TextAreaField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from .category import categories


class FeedbackForm(FlaskForm):

    name = StringField("Title:",validators=[InputRequired()])
    category = SelectField('Category', choices=categories.values())
    description = TextAreaField("Description", validators=[InputRequired()])