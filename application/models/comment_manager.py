import json, os
from schema import Comment
from application import db

def add_comment(data):
    comment = Comment(
        is_secret   = [0,1]['is-secret-comment' in data],
        content     = data['comment-content']
    )
    db.session.add(comment)
    db.session.commit()

def get_comment_by_id(post_id) :
    return Comment.query.get(post_id)

def update_profile_image(user_id, filename):
    user = get_user_by_id(user_id)
    user.profile_image = filename
    db.session.commit()