from flask import Blueprint, render_template, request
from app.db import cur, db
import mysql
import app.Service as Service
import json

user = Blueprint("users", __name__, template_folder="templates")

# @user.route('/')
# def usrse_page():
#     return "users page"


@user.route('/')
def users():
    cur.execute(
        '''SELECT *, users.id as users_uid from users left join department  
        on users.department_id = department.id''')
    data_list = cur.fetchall()

    return render_template('users.html', users=data_list)


@user.route('/mode/add')
def users_add():

    cur.execute('''SELECT * from department ''')
    result_list = cur.fetchall()

    return render_template('users_add.html', departments=result_list)


@user.route('/add', methods=["POST"])
def add_user():
    if request.method == "POST":
        name = str(request.form.get("name"))
        user_id = str(request.form.get("user_id"))
        user_pw = str(request.form.get("user_pw"))
        department_id = str(request.form.get("department_id"))

        if (not name or not user_id or not user_pw):
            return {"err": "err"}

        try:
            sql = f"insert into users(user_name, user_id, user_pw, create_datetime, department_id ) values( '{name}', '{user_id}', '{user_pw}', now(), null )"
            cur.execute(sql)
            db.commit()
        except Exception as e:
            return {"err": e}

        return {"message": "created new user"}
