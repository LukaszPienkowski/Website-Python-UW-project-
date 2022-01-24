import sqlite3
from flask import Blueprint, render_template, request, flash, jsonify, flash, redirect, session, abort, url_for
from flask import Flask
import numpy as np
import pandas as pd

views = Blueprint('views', __name__)

@views.route('/')
def lpage():
    return render_template('base.html')

@views.route('/home')
def main():
    return render_template("home.html")

@views.route('/employees')
def emp():
    return render_template("employees.html")            
   
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
    