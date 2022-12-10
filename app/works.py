from flask import Blueprint, render_template, request
from app.db import cur

work = Blueprint("works", __name__, template_folder="templates")

# @user.route('/')
# def usrse_page():
#     return "users page"


@work.route('/')
def users():
    cur.execute('''SELECT *, works.id as work_id from works 
    left join  users on works.create_user_id = users.id 
    left join department on users.department_id = department.id ''')

    print(cur)
    data_list = cur.fetchall()
    # print(data_list)

    return render_template('works.html', works=data_list)


@work.route('/mode/add')
def add_work_page():
    # print(request.form['id'])
    print("good")
    return render_template('works_add.html')


@work.route('/add', methods=["POST"])
def add_work():
    print(request.form)
    title = str(request.form['title'])
    due_date = str(request.form['due_date'])
    department_id = str(request.form['department_id'])
    text = str(request.form['text'])

    if (not title or not due_date):
        return {"err": "err"}

    print(title, due_date, department_id, text)
    return {"message": "add done"}
