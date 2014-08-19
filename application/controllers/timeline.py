from flask import render_template, session
from application import app
from application.models import user_manager, post_manager

@app.route('/timeline', defaults={'wall_id':0})
@app.route('/timeline/<int:wall_id>')
def timeline(wall_id):
	if request.method='POST' : 
		post_manager.add_post(request.form)

		return render_template('timeline.html', posts=[], timeline = {username : user_manager.get_user_by_id(wall_id).username})