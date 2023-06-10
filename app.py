from flask import Flask
homepage = Flask(__name__)

@homepage.route('/')
def home():
    return '<h1>Hello World..</h1>'

@homepage.route('/new')
def new():
    return '<h1>Hello New World..</h1>'

@homepage.route('/profile/<username>')
def profile(username):
    return '<h1>Hello %s..</h1>' %username

@homepage.route('/profile/<int:ProfileId>')
def profile1(ProfileId):
    return '<h1>Hello %d..</h1>' %ProfileId


homepage.run()