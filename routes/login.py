from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from . import routes
from .db import *

# Login-Đăng nhập
@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['txt_email']
        password = request.form['txt_password']

        user = User.query.filter_by(email=email).first()

        if ( password == user.password and email == user.email):
            return  render_template('home.html')
        else:
            return "Invalid username or password"

        return "Đăng nhập thành công"
    return render_template('login.html')


def get_obj_user(email, password):
    sqldbname = "../instance/booking_restaurant.db"
    result = None,

    conn = sqlite3.connect(sqldbname)
    cursor = conn.cursor()
    sqlcommand = "SELECT * FROM user WHERE email = ? and password = ?"
    obj_user = cursor.fetchone()
    if len(obj_user) > 0:
        result = obj_user
    conn.close()
    return result


@routes.route('/logout')
def logout():
    session.pop('current_user', None)
    # remove 'username' from the session
    return redirect(url_for('home'))



