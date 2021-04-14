from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField


class RegisterForm(FlaskForm):
    email = EmailField("Please input your email", validators=[DataRequired(), Email()])
    username = StringField("Please input your username", validators=[DataRequired()])
    password = PasswordField("input password", validators=[DataRequired()])