from flask import Blueprint, render_template, request, redirect
from app.db import cur

work = Blueprint("works", __name__, template_folder="templates")

# @user.route('/')
# def usrse_page():
#     return "users page"


@work.route('/')
def works():
    q = request.args.get('q', default="", type=str)
    sort = request.args.get('sort', default='DESC', type=str)

    if not sort.lower() in ['asc', 'desc']:
        sort = 'desc'
        print('sort desc')


    cur.execute(f'''SELECT *, works.id as work_id, works.create_datetime  as works_time, users.create_datetime  as users_time from works 
    left join  users on works.create_user_id = users.id 
    left join department on users.department_id = department.id 
    where works.title  like '%{q}%' order by works.create_datetime  {sort}   ''')
    data_list = cur.fetchall()

    return render_template('works.html', works=data_list , search_text = q)


@work.route('/<string:work_id>/')
def work_detail(work_id):
    cur.execute(
        f'''SELECT * ,works.id as work_id from works 
    left join users on works.create_user_id = users.id  
    where works.id  = {work_id}'''
    )
    result_work = cur.fetchone()
    if result_work:

        if result_work['is_done_by_who_id']:

            cur.execute(f''' 
            SELECT * from users where users.id  = {result_work['is_done_by_who_id']}
            ''')
            result_who_did = cur.fetchone()
            result_who_did.pop('user_pw', None)

        else:
            result_who_did = None

        # taks
        cur.execute(
            f'''SELECT * from tasks where tasks.parent_id  = {result_work['work_id']} order by due_date  ''')
        task_list = cur.fetchall()

        return render_template('works_detail.html', work=result_work, who_did=result_who_did, task_list=task_list)
    else:
        print("no work")
        return redirect('/works')


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
