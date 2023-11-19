from flask import render_template
from app1 import app

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
