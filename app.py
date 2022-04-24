from flask import Flask, render_template, request, redirect, url_for, session,abort
from flask_mysqldb import MySQL
import logging
from flaskCreate import app
from errorhandling import error
import MySQLdb.cursors
import re
import secrets
import os


logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# app.secret_key = secrets.token_hex(16)
# database Initialize in another file
# app.config['MYSQL_HOST'] = 'us-cdbr-east-05.cleardb.net'
# app.config['MYSQL_USER'] = 'bb09d462c08d07'
# app.config['MYSQL_PASSWORD'] = '2979179c'
# app.config['MYSQL_DB'] = 'heroku_4176c403d4233e5'
# mysql = MySQL(app)

@app.route('/')
def index():
    #TODO:  check for session log in first
    app.logger.info('Fetch index.html template')
    return render_template('index.html')
        
@app.route('/profile')
def profile():
    #TODO:  check for session log in first
    return render_template('my-profile.html')

@app.route('/jobapplication')
def jobapplication():
    #TODO:  check for session log in first
    return render_template('job-application.html')

@app.route('/joblist')
def joblist():
    #TODO:  check for session log in first
    return render_template('job-list.html')

@app.route('/jobview')
def jobview():
    #TODO:  check for session log in first
    return render_template('job-view.html')

@app.route('/newjob')
def newjob():
    #TODO:  check for session log in first
    return render_template('new-job.html')


if __name__ == '__main__':
   app.run()