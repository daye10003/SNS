import json, os
from schema import User
from application import db

# LOGIN WITH EMAIL & PASSWORD
def get_user_by_email(email) :
    '''
    [INPUT]
    email : user-email
    [TODO]
    1. get user instance from database SEARCH WITH email
    2. return that instance
    '''
    return User.query.filter(User.email==email).first()

def get_user_by_id(user_id) :
    '''
    [INPUT]
    user_id : primary key of User Table
    [OUTPUT]
    if exists : User row
    else      : None
    '''
    return User.query.get(user_id)

def add_user(data) :
    '''
    [INPUT]
    data <= request.form
    [TODO]
    1. MAKE User instance
    user = User(email = data['email'], password = data['password'], ...)
    2. add user instance to database session
    3. commit to database
    '''
    user = User(
        email    = data['email'],
        password = db.func.md5(data['password']),
        username = data['username'],
        mobile   = data['mobile'],
        gender   = data['gender'],
        birthday = data['birthday']
    )
    db.session.add(user)
    db.session.commit()

def auth_check(email, password) :
    '''
    [INPUT]
    email <= request.form['email']
    password <= request.form['password']

    '''
def auth_check(data) :
    '''
    [INPUT]
    data <= request.form <= form from HTML
    [OUTPUT]
    return [True/False]
    [TODO]
    1. email -> email
    2. password -> encrypt with db.func.md5
    3. get user row with email & encrypted passwordfrom db
    4. return True if row exists else False
    '''
    password=db.func.md5(data['password'])
    email=data['email']
    if User.query.filter(User.email==email, User.password==password).first()==None:
        return False
    else:
        return True

def update_profile_image(user_id, filename):
    user = get_user_by_id(user_id)
    user.profile_image = filename
    db.session.commit()
