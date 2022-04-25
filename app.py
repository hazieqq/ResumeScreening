from flask import Flask, render_template, request, redirect, url_for, session,abort
from flask_mysqldb import MySQL
import logging
from flaskCreate import app
from errorhandling import error
import MySQLdb.cursors


logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


# mysql initialization
mysql = MySQL(app)

@app.route('/')
def index():
    #TODO:  check for session log in first
    app.logger.info('Fetch index.html template')
    return render_template('index.html')
        
@app.route('/profile')
def profile():
    #TODO:  check for session log in first
    app.logger.info('Fetch my-profile.html template')
    return render_template('my-profile.html')

@app.route('/application')
def application():
    #TODO:  check for session log in first
    app.logger.info('Fetch job-application.html template')
    return render_template('job-application.html')

@app.route('/joblist')
def joblist():
    #TODO:  check for session log in first
    app.logger.info('Fetch job-list.html template')
    return render_template('job-list.html')

@app.route('/jobview')
def jobview():
    #TODO:  check for session log in first
    app.logger.info('Fetch job-view.html template')
    return render_template('job-view.html')

@app.route('/newjob')
def newjob():
    #TODO:  check for session log in first
    app.logger.info('Fetch new-job.html template')
    return render_template('new-job.html')


@app.route('/submitNewJobPost', methods=["GET","POST"])
def submitNewJobPost():
    position = request.values.get('data')
    print(position,"adsdadsdadadad")
    app.logger.info('position: ',position)
    return "1"


if __name__ == '__main__':
   app.run()