#blog.py - controller

#imports
from flask import Flask, render_template, request, session, flash, redirect, \
    url_for, g
import sqlite3

#configuration
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '<85>÷n`Df°EÐ    ^Fa<89>Ùæ^FÀ<8e><90><9f><8f>^A>q'
DATABASE = 'blog.db'

app = Flask(__name__)

#pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

#function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
            request.form['password'] != app.config['PASSWORD']:
                error = 'Invalid Credentials. Please try again.'
            else:
                session['logged_in'] = True
                return redirect(url_for('main'))
        return render_template('login.html', error=error)

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)

