from flask import render_template, session, request
from application import app
from application.models import user_manager, post_manager, comment_manager
from bs4 import BeautifulSoup as BS

def render_comment(comment):
	return render_template('comment.html', comment=comment)

def render_post(post):
	comment_list = []
	comments = comment_manager.get_comment_by_id(post.id)
	session_username = user_manager.get_user_by_id(session['user_id']).username
	if comments :
		for comment in comments :
			comment_list.append(render_comment(comment))
	return render_template('post.html', comments=comment_list, post=post, session_username=session_username)

def render_timeline(wall_id):
	post_list = []
	posts = post_manager.get_post(wall_id)
	wall_owner = user_manager.get_user_by_id(wall_id)
	user=session['user_id']
	if posts :
		for post in posts:
			post_list.append(render_post(post))
	return render_template('timeline.html', posts = post_list, wall_owner=wall_owner, user=user)

@app.route('/timeline/', defaults={'wall_id':0}, methods=['GET', 'POST'])
@app.route('/timeline/<int:wall_id>', methods=['GET', 'POST'])
def timeline(wall_id):
	if wall_id == 0 : wall_id = session['user_id']
	if request.method=='POST' : 
		if 'post-content' in request.form :
			# New Posting
			post_manager.add_post(request.form, wall_id)
		elif 'comment-content' in request.form :
			# New Comment
			comment_manager.add_comment(request.form)	
	return render_timeline(wall_id)