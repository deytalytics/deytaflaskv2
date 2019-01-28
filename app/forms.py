#Import web forms
from wtforms import Form, BooleanField, StringField, TextField, PasswordField, validators
from flask_wtf import FlaskForm 
from wtforms.validators import InputRequired, Email, Length
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask import session
from app import app
from app.models import Deypay_user
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	return Deypay_user.query.get(int(user_id))

def check_user_password(form, field):
	user = Deypay_user.query.filter_by(username=form.username.data).first()
	if user:
		if check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			session['username']=form.username.data
		else: 
			raise validators.ValidationError('Username or Password is incorrect')
	else:
		raise validators.ValidationError('Username or Password is incorrect')
	
class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15), check_user_password])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), validators.EqualTo('confirm', message='Passwords must match'), Length(min=8, max=20)])
	confirm = PasswordField('confirm', validators=[InputRequired(), Length(min=8, max=20)])
