from application import app
from flask import render_template, session
from application.models import user_manager
@app.route('/')
def index() :
	if 'logged_in' in session:
		user = user_manager.get_user_by_id(session['user_id'])
	return render_template('index.html', user=user)