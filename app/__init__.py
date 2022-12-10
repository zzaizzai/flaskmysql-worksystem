from flask import Flask, jsonify, request, render_template, Blueprint
from app.db import cur
from app.users import user
from app.works import work

app = Flask(__name__)
app.register_blueprint(user, url_prefix="/users")
app.register_blueprint(work, url_prefix="/works")



# from .models import users

@app.route('/')
def home():
    cur.execute("select * from users")
    data_list = cur.fetchall()
    print(data_list)
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
