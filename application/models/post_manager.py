import json, os
from schema import User
from application import db

def add_post(data):
	post = Post(
		is_secret	= data['is_secret'],
		content		= data['content']
	)
	db.session.add(post)
	db.session.commit



	