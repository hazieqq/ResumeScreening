from flask import Flask, render_template, request, redirect, url_for, session,abort
import logging
from flaskCreate import app
from errorhandling import error
import MySQLdb.cursors
from db import DB

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')



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
    jobApply = DB.readFromJobApply()
    # throw exception flow if database cant access !
    abort(500) if jobApply == "fail" else ""
    user1 = ()
    for i in range(len(jobApply)):
        # user is in a form of tupple
        user = DB.readFromUserAccount(jobApply[i]["userID"])
        abort(500) if user == "fail" else  ""
        user1 += user
    app.logger.info(jobApply)
    app.logger.info(user1)
    return render_template('job-application.html',jobApply=jobApply,user=user1)

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


@app.route('/submitNewJobPost', methods=["POST"])
def submitNewJobPost():
    # pre-check all values in sweetAlert.js
    title = request.values.get('title')
    category = request.values.get('category')
    jobtype = request.values.get('jobtype')
    vacancy = request.values.get('vacancy')
    experience = request.values.get('experience')
    date = request.values.get('date')
    salaryFrom = request.values.get('salaryFrom')
    salaryTo = request.values.get('salaryTo')
    qualification = request.values.get('qualification')
    description = request.values.get('description')
    status1 = request.values.get('status1')
    response = DB.insertIntoJobPost(title,category,jobtype,vacancy,experience,date,salaryFrom,qualification,description,status1)
    
    return response


if __name__ == '__main__':
   app.run()