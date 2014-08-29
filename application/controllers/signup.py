from flask import url_for, render_template, flash, request
from application import app
from application.models import user_manager

from flask.ext.wtf import Form
from wtforms import(
	StringField,
	PasswordField,
	DateField
	)
from wtforms import validators

class UserForm(Form) :
	email = StringField(
		u'email',
		[
			validators.data_required(message=u'please enter email'),
			validators.Email(message='use email form')
		],
		description = {'placeholder': u'username@email.com'}
	)
	password = PasswordField(
		u'password',
		[
			validators.data_required(message=u'please enter password'),
			validators.Length(min=6, max=20),
			validators.EqualTo('password_check', message=u'password does not match')
		],
		description = {'placeholder' : u'password'}
	)
	password_check = PasswordField(
		u'password check',
		[
			validators.data_required(message=u'please confirm your password')		
		],
		description = {'placeholder' : u'password check'}
	)
	username = StringField(
		u'username',
		[
			validators.data_required(message=u'please enter username'),
			validators.Length(min=3, max=10)
		],
		description = {'placeholder' : u'username'}
	)
	# mobile = 
	# gender = 
	# birthday = DateField(
	# 	'Posted Date (mm/dd/yyyy)',validators=[required()],format='%m/%d/%Y'))


@app.route('/signup', methods = ['GET', 'POST'])
def signup() :
	if request.method == 'POST' :
		form = UserForm()
		if form.validate_on_submit():
			if user_manager.is_email_duplicated(request.form['email'])==True:
				return render_template('signup.html', form=form, signup_error='existing email')
			else:
				user_manager.add_user(request.form)
				flash('Sign up successful!')
				return render_template('index.html', form=form)
		else:
			return render_template('signup.html', form=form, signup_error=signup_error)
	else :
		form=UserForm()
		return render_template('signup.html', form=form)


'''
REQUEST

1. GET

2. POST

[RECEIVER]
nothing
=> GET only

methods = ['POST']
=> POST only

methods = ['GET', 'POST']
=> Both GET and POST 

[SENDER]
<form action="url" method="post">
	<~>
		<input type="~" name="~"/>
		...
	</~>
	<~>
		<input type="~" name="~"/>
		...
	</~>
	<~>
		<input type="~" name="~"/>
		...
	</~>
	<input type="submit" value="$$%^#$%"/>
</form>

'''