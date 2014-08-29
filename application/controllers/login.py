from flask import render_template, url_for, redirect, flash, session, request
from application import app
from application.models import user_manager
import re
from flask.ext.wtf import Form
from wtforms import	StringField, PasswordField, validators

class UserForm(Form) :
	email = StringField(
		u'email',
		[
			validators.data_required(message=u'please enter email'),
			validators.Email(message='use email form')

		],
		description = {'placeholder': u'email'}
	)
	password = PasswordField(
		u'password',
		[
			validators.data_required(message=u'please enter password'),
		],
		description = {'placeholder' : u'password'}
	)

@app.route('/login', methods=['POST', 'GET'])
def login() :
	if request.method == 'POST' :
		form = UserForm()
		if form.validate_on_submit():
			is_valid=user_manager.auth_check(form.data)
			if is_valid :
				user = user_manager.get_user_by_email(request.form['email'])
				# session.pop(wall_id)
				session['logged_in'] = True
				session['user_id'] = user.id
				session['email'] = request.form['email']
				session['username'] = user.username
				return redirect(url_for('timeline', wall_id=user.id, user = user))
			else :
				login_error = 'Invalid id or password'
				return render_template('login.html', form=form, login_error=login_error)
		else:
			return render_template('login.html', form=form)

	else :
		form=UserForm()
		return render_template('login.html', form=form)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	session.pop('user_id', None)
	session.pop('email', None)
	session.pop('username', None)
	flash('You were logged out')
	return redirect(url_for('index'))