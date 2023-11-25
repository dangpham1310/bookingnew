from flask import render_template, request
from flask import Flask,jsonify, render_template, request, redirect, url_for, session
from . import routes
from .db import Booking
from routes.db import *

@routes.route('/booking', methods=["POST", "GET"])
def booking():
    if request.method == 'POST':
        hoten = request.form['name']
        sdt = request.form['sdt']
        email = request.form['email']
        songuoi = request.form['songuoi']
        soban = request.form['soban']
        ngaybook_str = request.form['ngaybook']
        giobook_str = request.form['giobook']
        nhahang = request.form['nhahang']

    # Convert the string date to a Python date object
        ngaybook = datetime.strptime(ngaybook_str, '%Y-%m-%d').date()
        giobook = datetime.strptime(giobook_str, '%H:%M').time()
        # Insert data into the database
        new_booking = Booking(name=hoten, sdt=sdt, email=email, songuoi=songuoi,
                            soban=soban, ngaybook=ngaybook, giobook=giobook,
                            nhahang=nhahang)
        db.session.add(new_booking)
        db.session.commit()

        return render_template('result.html', name=hoten, sdt=sdt, email=email,
                        songuoi=songuoi, soban=soban, ngaybook=ngaybook,
                        giobook=giobook, nhahang=nhahang)
    return render_template('booking.html')