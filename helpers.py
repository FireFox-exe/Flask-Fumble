from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField,PasswordField

class GameForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    category = StringField('Category',[validators.DataRequired(), validators.Length(min=1, max=40)])
    company = StringField('Company', [validators.DataRequired(), validators.Length(min=1, max=50)])
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')

class UserForm(FlaskForm):
    nickname = StringField('nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    password = PasswordField('password', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('login')

