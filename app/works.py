from flask import Blueprint,render_template
from app.db import cur

work = Blueprint("works", __name__, template_folder="templates")

# @user.route('/')
# def usrse_page():
#     return "users page"
    

@work.route('/')
def users():
    cur.execute("select * from works")

    print(cur)
    data_list = cur.fetchall()
    print(data_list)

    
    return render_template('works.html', works=data_list)