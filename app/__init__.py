from flask import Flask, jsonify, request, render_template
from app import db

cur = db.cur

app = Flask(__name__)


@app.route('/')
def home():
    cur.execute("select * from users")
    data_list = cur.fetchall()
    print(data_list)

    return render_template('index.html', message=data_list)

@app.route('/users')
def users():
    cur.execute("select * from users")
    data_list = cur.fetchall()
    print(data_list)
    return render_template('users.html')

@app.route('/index')
def index():
    message = 'hello bro'
    return render_template('index.html', message=message)

@app.errorhandler(404)
def show404(error):
    return render_template('404.html'), 404

