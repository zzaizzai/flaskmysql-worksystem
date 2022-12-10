from flask import Blueprint, render_template, request
from app.db import cur, db
import mysql
import app.Service as Service
import datetime
import jwt

SECRET_KEY = 'SPARTA'

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route('/', methods=["GET"])
def show_login_page():
    if request.method == "GET":
        try:
            token_receive = request.cookies.get('mytoken')
            payload = jwt.decode(token_receive, SECRET_KEY,
                                 algorithms=['HS256'])
            print(payload)
        except Exception as e:
            print(e)
        return render_template('login.html')


@auth.route('/mypage', methods=["GET"])
def mypage():

    try:
        token_receive = request.cookies.get('mytoken')
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        sql = f'''SELECT * from users LEFT JOIN
          department  on users.department_id = department.id  
          where user_id = "{payload['id']}"  limit 1'''
        cur.execute(sql)
        data_list = cur.fetchall()
        if len(data_list) == 1:
            return render_template('mypage.html', user=data_list[0])
        else:
            return "none"

    except Exception as e:
        print(e)
        return render_template('login.html', message="please login")


@auth.route('/login', methods=["POST"])
def login():
    print(request.form['id'])
    print(request.form['pw'])
    id_receive = request.form['id']
    pw_receive = request.form['pw']

    sql = f"SELECT * from users where user_id = '{id_receive}' and user_pw = '{pw_receive}' limit 1"
    cur.execute(sql)
    result = cur.fetchall()
    print(result)

    if len(result) == 1:
        print("good")

        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)  # 언제까지 유효한지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return {'result': 'success', 'token': token}
    else:
        return {'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'}
