from application import app
from flask import render_template, request, redirect, url_for, session
from application.models import file_manager, user_manager
import os

@app.route('/profile')
def profile():
	user = user_manager.get_user_by_id(int(session['user_id']))
	return render_template('profile.html', user = user)

@app.route('/upload_image', methods=['POST'])
def upload_image():
	image_file = request.files['profile-image']
	filename = image_file.filename

	file_path = '/gs/daye10003/profile/%s.%s'%(str(session['user_id']), filename.split('.')[-1])
	file_manager.save_file(image_file, file_path)
	user_manager.update_profile_image(session['user_id'], file_path.split('/')[-1])
	return render_template('profile.html', user = user_manager.get_user_by_id(int(session['user_id'])))

@app.route('/image/profile', methods=['POST'])
def get_profile_image(filename) :
	file_path = os.path.join('/gs/daye10003', 'profile', filename)
	return file_manager.read_file(file_path)