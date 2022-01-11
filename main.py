from os import name
import sqlite3
from flask.templating import render_template
from flask.wrappers import Request
from werkzeug.wrappers import request
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

conn = sqlite3.connect('login.db')

#conn.execute('') kwerendy here