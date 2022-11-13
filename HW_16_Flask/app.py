# -------------------------------------------------------
# Program by Mikhail Katsar (ankiav)
#
# Version       Date            Info
# 0.0.1         07/11/2022      First flask app
# -------------------------------------------------------


from flask import render_template, request, redirect, url_for
import sys
from werkzeug.security import generate_password_hash
import pymysql

from settings import HOST
from settings import PORT
from settings import DEBUG
from settings import USER_DB
from settings import PASSWORD_DB
from settings import HOST_DB
from settings import NAME_DB
from settings import app

from models import db, Users, Profiles


# start and homepage
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


# /about page from old html5 project
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/database')
def database():

    try:
        con = pymysql.connect(
            host=HOST_DB,
            user=USER_DB,
            password=PASSWORD_DB,
            db=NAME_DB,
            use_unicode=True,
            charset='utf8',
        )
        print('+=========================+')
        print('|  CONNECTED TO DATABASE  |')
        print('+=========================+')
    except Exception as err:
        sys.exit('error', err)

    cur = con.cursor()
    cur.execute("SELECT * FROM profiles")
    data = cur.fetchall()
    return render_template('database.html', data=data)


@app.route("/register", methods=("POST", "GET"))
def register():
    if request.method == "POST":
        # здесь должна быть проверка корректности введенных данных
        try:
            hash = generate_password_hash(request.form['psw'])
            u = Users(email=request.form['email'], psw=hash)
            db.session.add(u)
            db.session.flush()

            p = Profiles(
                name=request.form['name'],
                age=request.form['age'],
                city=request.form['city'],
                user_id=u.id
            )
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")

        return redirect(url_for('database'))
    return render_template("register.html")


if __name__ == "__main__":
    # app.debug = True
    # app.env = "ankiav working hard!"
    app.run(HOST, PORT, DEBUG)
