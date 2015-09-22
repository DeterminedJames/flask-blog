#blog.py - controller
#This Python file uses the following encoding: utf-8
#imports
from flask import Flask, render_template, request, session, flash, redirect, \
    url_for, g
import sqlite3
from functools import wraps

#configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '<85>÷n`Df°EÐ    ^Fa<89>Ùæ^FÀ<8e><90><9f><8f>^A>q'

app = Flask(__name__)

#pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

#function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

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

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route('/main')
@login_required
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)

