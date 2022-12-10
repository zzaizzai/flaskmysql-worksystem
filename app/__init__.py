from flask import Flask, jsonify, request, render_template, Blueprint
from app.db import cur
from app.users import user
from app.works import work
from app.auth import auth

app = Flask(__name__)
app.register_blueprint(user, url_prefix="/users")
app.register_blueprint(work, url_prefix="/works")
app.register_blueprint(auth, url_prefix="/auth")

# from flask_login import LoginManager
# login_manager = LoginManager()

# login_manager.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users/mode/add')
def users_add():
    return render_template('users_add.html')


@app.route('/index')
def index():
    message = 'hello bro'
    return render_template('index.html', message=message)


@app.errorhandler(404)
def show404(error):
    return render_template('404.html'), 404
