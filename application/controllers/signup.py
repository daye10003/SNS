from flask import url_for, render_template, flash, request
from application import app
from application.models import user_manager

@app.route('/signup', methods = ['GET', 'POST'])
def signup() :
	if request.method == 'POST' :
		user_manager.add_user(request.form)
		flash('Sign up successful!')
		return render_template('index.html')
	else :
		return render_template('signup.html')

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