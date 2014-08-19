from flask import render_template, url_for, redirect, flash, session, request
from application import app
from application.models import user_manager

@app.route('/login', methods=['POST', 'GET'])
def login() :
	if request.method == 'POST' :
		is_valid = user_manager.auth_check(request.form)
		if is_valid :
			user = user_manager.get_user_by_email(request.form['email'])
			session['logged_in'] = True
			session['user_id'] = user.id
			session['email'] = request.form['email']
			session['username'] = user.username
			return render_template('timeline.html')
		else :
			flash('Invalid')
			return redirect(url_for('login'))
	else :
		return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('index'))