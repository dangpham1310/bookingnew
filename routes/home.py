from datetime import datetime
from flask import Flask, flash, render_template, request, redirect, session, url_for
import sqlite3
from . import routes
from .db import*
@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email đã tồn tại. Vui lòng chọn email khác.', 'error')
            return redirect(url_for('routes.register'))
        user = User(name = name,password = password,email = email,phone = phone)
        db.session.add(user)
        db.session.commit()
        register_success = "Đăng kí thành công!!"
        print(register_success)
        flash("Bản ghi đã được thêm", "Thành công")
        return redirect(url_for('routes.login'))


    return render_template('register.html')





