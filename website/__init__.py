from flask import Flask, url_for
import sqlite3

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5J8I25HEgSJaPdR4nPR6FUjkDx5BBUWP'

    from .views import views
    from .dbf import dbf

    app.register_blueprint(dbf, url_prefix = '/')
    app.register_blueprint(views, url_prefix='/')

    return app
