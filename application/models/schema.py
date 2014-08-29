from application import db

class User(db.Model):
	id			= db.Column(db.Integer, primary_key = True)
	username	= db.Column(db.String(45))
	email		= db.Column(db.String(45))
	password	= db.Column(db.String(100))
	gender		= db.Column(db.Enum('F','M'))
	mobile		= db.Column(db.String(15))
	birthday	= db.Column(db.Date)
	profile_image = db.Column(db.String(100))

class Post(db.Model):
	id			= db.Column(db.Integer, primary_key = True)
	user_id 	= db.Column(db.Integer, db.ForeignKey('user.id')) 
	wall_id		= db.Column(db.Integer, db.ForeignKey('user.id'))	
	edited_time	= db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())
	created_time= db.Column(db.DateTime, default = db.func.now())
	is_edited 	= db.Column(db.Boolean, default = '0', onupdate = '1')
	is_secret	= db.Column(db.Boolean, default = '0')
	content		= db.Column(db.Text())
	user 		= db.relationship('User', foreign_keys = [user_id])
	wall 		= db.relationship('User', foreign_keys = [user_id], backref = db.backref('wall_posts', cascade = 'all, delete-orphan', lazy = 'dynamic'))

class Comment(db.Model):
	id 			= db.Column(db.Integer, primary_key = True)
	user_id 	= db.Column(db.Integer, db.ForeignKey('user.id'))
	post_id 	= db.Column(db.Integer, db.ForeignKey('post.id'))
	user 		= db.relationship('User')
	post  		= db.relationship('Post', backref = db.backref('comments', cascade = 'all, delete-orphan', lazy = 'dynamic'))
	created_time= db.Column(db.DateTime, default = db.func.now())
	content		= db.Column(db.Text())
	is_secret	= db.Column(db.Boolean, default = '0', onupdate = '1')