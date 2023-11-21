from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username=StringField('useename1',validators=[DataRequired()])
	password=PasswordField('input passworx',validators=[DataRequired()])
	remember_me=BooleanField('Remmbee me')
	submit=SubmitField('sign in')
