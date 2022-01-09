from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

##Tu trzeba podpiąć logowanie do bazy danych (te z base.html)