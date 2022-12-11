from flask import Blueprint, render_template, request, redirect
from app.db import cur, db
import mysql
import app.Service as Service
import json

task = Blueprint("tasks", __name__, template_folder="templates")


@task.route('/')
def tasks_page():

    cur.execute(''' SELECT * from tasks  ''')
    task_list = cur.fetchall()

    return render_template('tasks.html', task_list=task_list)


@task.route('/mode/add')
def task_mode_add():
    parent_id = request.args.get('parent_id', default=None, type=str)
    print(parent_id)

    # Check parent_id
    if parent_id == None:
        print('nop')
        return redirect('/works')
    cur.execute(f''' SELECT 	* from works where works.id  = {parent_id} ''')
    parent_work = cur.fetchone()

    cur.execute('''SELECT * from department ''')
    department_list = cur.fetchall()

    return render_template('tasks_add.html',
                           department_list=department_list,
                           parent_work=parent_work)


@task.route('/<task_id>/')
def task_detail(task_id):
    cur.execute(f'''SELECT * from tasks where tasks.id = {task_id} ''')
    result_task = cur.fetchone()

    print(result_task)

    if result_task == None:
        return redirect('/works')

    return render_template('tasks_detail.html', task=result_task)


@task.route('/add', methods=["POST"])
def add_new_task():
    print(request.form)

    parent_id = request.form['parent_id']
    title = request.form['title']
    department_id = request.form['department_id']
    due_date = request.form['due_date']
    text = request.form['text']

    if not title or not department_id or not parent_id:
        return {"err": "check input"}

    try:
        sql = f'''INSERT into tasks(parent_id , title, charge_department_id  , due_date, create_datetime) 
        values ({parent_id}, "{title}", {department_id} , "{due_date}", now() )  '''
        cur.execute(sql)
        db.commit()
        return {"message":  "good"}
    except Exception as e:
        return {"err": e}

    return {"message":  "good"}
