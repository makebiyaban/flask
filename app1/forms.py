from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username=StringField('username',validators=[DataRequired()])
	password=PasswordField(label='input password',validators=[DataRequired()])
	remember_me=BooleanField('Remmber me')
	submit=SubmitField('sign in')
