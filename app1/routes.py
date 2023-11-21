from flask import render_template,flash,redirect,url_for
from app1 import app
from app1.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
	user={'name':'mohammad'}
	posts=[
		{'author':{'username':'ali'},
		 'body':'yek rooz ziba dar tehran'},
		{'author':{'username':'ziba'},
   		 'body':'che film khobi bood'
		}
	]
	return render_template('index.html',user=user,title='Home',posts=posts)
	
@app.route('/login', methods = ['POST','GET'])
def login():
	form=LoginForm()
	if form.validate_on_submit() :
		flash ('Login requested for user {}, remember_me={}'.format(form.username.data,form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html',title='sign in',form=form)
