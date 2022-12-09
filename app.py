from flask import Flask, jsonify, request, render_template
from sqlalchemy import create_engine, text
import pymysql
import config
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_USER = os.environ.get("DB_USER")
HOST = os.environ.get("HOST")
TABLE = os.environ.get("TABLE")
USER_PW = os.environ.get("USER_PW")


db = mysql.connector.connect(
    host=HOST,
    user=DB_USER,
    passwd=USER_PW,
    db=TABLE,
)

cur = db.cursor()

app = Flask(__name__)


@app.route('/')
def home():
    cur.execute("select * from users")
    data_list = cur.fetchall()
    print(data_list)

    return render_template('index.html', message=data_list)


@app.route('/index')
def index():
    message = 'hello bro'
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
