import sqlite3
from flask import Flask, Blueprint, render_template, request, flash, jsonify, flash, redirect, session, abort, url_for
import numpy as np
import pandas as pd


dbf = Blueprint('dbf', __name__)


@dbf.route('/employees', methods = ["GET", "POST"])            
def list():   
    con = sqlite3.connect("PythonProject.db")
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    cur.execute("SELECT * FROM Employees")
   
    rows = cur.fetchall(); 
    return render_template("employees.html", rows = rows)



@dbf.route('/', methods = ['GET', 'POST'])
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
                return char2()
            else:
                msg = "Please enter valid email and password"
    return render_template('base.html', msg = msg)
def logout():
    session.clear()
    return render_template('base.html')


@dbf.route('/clients', methods = ["GET", "POST"])            
def listcl():   
    con = sqlite3.connect("PythonProject.db")
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    cur.execute("SELECT * FROM Clients")
    rows = cur.fetchall(); 

    cur.execute("SELECT * FROM Projects")
    rows1 = cur.fetchall()

    con.close()
    return render_template("clients.html", rows = rows, rows1 = rows1)


@dbf.route('/money_transfers', methods = ["GET", "POST"])            
def listmt():   
    con = sqlite3.connect("PythonProject.db")
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    cur.execute("SELECT * FROM MoneyTransfers")
   
    rows = cur.fetchall(); 
    return render_template("money_transfers.html", rows = rows)


@dbf.route('/invoices', methods = ["GET", "POST"])            
def listinv():   
    con = sqlite3.connect("PythonProject.db")
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    cur.execute("SELECT * FROM Invoices")
   
    rows = cur.fetchall(); 
    return render_template("invoices.html", rows = rows)

@dbf.route('/home', methods = ["POST", "GET"])
def char2():
    con = sqlite3.connect("PythonProject.db")
    cur = con.cursor()
    df = pd.read_sql_query("SELECT * FROM MoneyTransfers ORDER BY Date", con)
    temp = df["Amount"].tolist()
    for i in range(len(df["InOut"])):
        if df['InOut'][i] == 1:
            temp[i] = temp[i]*-1
    list = [df["Date"].tolist(), temp]
    dates = list[0]
    amounts = list[1]
    
    df = pd.read_sql_query("SELECT * FROM Projects", con)
    values = []
    values.append(len(df.loc[df['Date'] == 2021]))
    values.append(len(df.loc[df['Date'] == 2020]))
    values.append(len(df.loc[df['Date'] == 2019]))
    values.append(len(df.loc[df['Date'] == 2018]))
    labels = ['2021', '2020', '2019', '2018'] 

    amn = [2, 1, 1]
    names = ['Poland', 'Germany', 'Czech Republic']

    return render_template("home.html", dates = dates, amounts = amounts, values = values, labels = labels, names = names, amn = amn)

@dbf.route('/view', methods = ['GET', 'POST'])
def view():
    con = sqlite3.connect("PythonProject.db")
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    cur.execute("SELECT * FROM YearBalance")
   
    rows = cur.fetchall(); 
    return render_template("view.html", rows = rows)

