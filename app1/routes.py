from flask import render_template
from app1 import app

@app.route('/')
@app.route('/indec')
def index():
	user={'name':'mohammad'}
	return render_template('index.html',user=user)
