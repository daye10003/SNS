from application import app
from flask import render_template, request

@app.route('/request_example', methods=['POST', 'GET'])
def request_example() :
	if request.method == 'POST' :
		return render_template(
			'request_example.html',
			message = 'POST_REQUEST WITH email : %s, password : %s' % (request.form['email'], request.form['password'])
		)
	else :
		return render_template('request_example.html', message = 'BASIC')