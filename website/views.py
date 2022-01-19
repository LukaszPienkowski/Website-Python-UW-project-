import sqlite3
from flask import Blueprint, render_template, request, flash, jsonify, flash, redirect, session, abort, url_for
from flask import Flask
import numpy as np
import pandas as pd

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def login():
    r = ''
    msg = ''
    if(request.method == 'POST'):
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('signup.db')
        c = conn.cursor()
        c.execute("SELECT * FROM person WHERE email = '" +email+"' and password = '"+password+"'")
        r = c.fetchall()
        for i in r:
            if(email == i[0] and password == i [1]):
                session['logedin'] = True
                session['email'] = email
                return render_template('home.html')
            else:
                msg = "Please enter valid email and password"
    return render_template('base.html', msg = msg)
def logout():
    session.clear()
    return render_template('base.html')

@views.route('/home')
def main():
    return render_template('home.html')

@views.route('/employees')
def emp():
    return render_template('employees.html')
   
@views.route('/clients')
def cl():
    return render_template('clients.html')

@views.route('/structure')
def st():
    return render_template('structure.html')

@views.route('/invoices')
def inv():
    return render_template('invoices.html')

@views.route('/money_transfers')
def tr():
    return render_template('money_transfers.html')    
    