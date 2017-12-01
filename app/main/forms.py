from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, PasswordField
from wtforms.validators import Required, Length, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(), Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Login')


