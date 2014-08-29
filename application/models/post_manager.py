import json, os
from schema import Post
from application import db
from flask import session

def add_post(data, wall_id):
	post = Post(
		is_secret = [0,1]['is-secret-post' in data],
		content		= data['post-content'],
		wall_id		= wall_id,
		user_id		= session['user_id']
	)
	db.session.add(post)
	db.session.commit()

def get_post(wall_id):

	return Post.query.filter(Post.wall_id==wall_id).all()
	
  