from flask import Flask, render_template, request, redirect, url_for, session,abort,jsonify
import logging
from flaskCreate import app
from errorhandling import error
from db import DB
from datetime import date

#logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')





@app.route('/api/v1/resources/events/all', methods=['GET'])
def api_all():
    dateline = DB.fetchDateline()
    title = dateline[0]['title']
    print(dateline[0]['closeddate'])
    events= [
        {
            'title': title,
            'start': '2022-02-10',
            'className': "bg-danger"
        },
        
    ]
    return jsonify(events)


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
    
    # make applicantStatus lower because flask does not have lower function
    for x in range(len(jobApply)):
        jobApply[x]["applicantStatus"] = jobApply[x]["applicantStatus"].lower() 
    
    user1 = ()
    for i in range(len(jobApply)):
        # user is in a form of tupple
        user = DB.readFromUserAccount(jobApply[i]["userID"])
        abort(500) if user == "fail" else  ""
        user1 += user
        
    app.logger.info(jobApply)
    app.logger.info(user1)
    return render_template('job-application.html',jobApply=jobApply,user=user1,dashboard="Application")

@app.route('/joblist')
def joblist():
    #TODO:  check for session log in first
    app.logger.info('Fetch job-list.html template')
    jobPost = DB.readFromJobPost()
    
    # throw exception flow if database cant access !
    abort(500) if jobPost == "fail" else ""
    
    print(jobPost)
    return render_template('job-list.html',jobPost=jobPost)

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

@app.route('/shortlistCandidate')
def shortlistCandidate():
    #TODO:  check for session log in first
    app.logger.info('Fetch shortlistCandidate.html template')
    return render_template('shortlistCandidate.html')

@app.route('/calender')
def calender():
    #TODO:  check for session log in first
    app.logger.info('Fetch calender.html template')
    return render_template('calender.html')

@app.route('/submitNewJobPost', methods=["POST"])
def submitNewJobPost():
    # pre-check all values in sweetAlert.js
    title = request.values.get('title')
    jobtype = request.values.get('jobtype')
    experience = request.values.get('experience')
    closedDate = request.values.get('date')
    salaryFrom = request.values.get('salaryFrom')
    description = request.values.get('description')
    status1 = request.values.get('status1')
    postedDate = date.today()
    response = DB.insertIntoJobPost(title,jobtype,experience,closedDate,postedDate,salaryFrom,description,status1)
    
    return response


@app.route('/delete', methods=["POST"])
def delete():
    response = "fail"
    if request.values.get('deletefrom') == 'application':
        id = request.values.get('id')
        response = DB.deleteJobApply(id)
    elif request.values.get('deletefrom') == 'joblist':
        id = request.values.get('id')
        response = DB.deleteJobList(id)
    return response


@app.route('/update', methods=["POST"])
def update():
    # declare response as fail first !
    response = "fail"
    if request.values.get('update') == 'updateStatus':
        jobapplyID = request.values.get('jobapplyID')
        text = request.values.get('text')
        response = DB.updateJobApply(jobapplyID,text)
    elif request.values.get('update') == 'updateJobList':
        id = request.values.get('id')
        title = request.values.get('title')
        type = request.values.get('type')
        salary = request.values.get('salary')
        postedDate = request.values.get('postedDate')
        closedDate = request.values.get('closedDate')
        status = request.values.get('status')
        description = request.values.get('description')
        exp = request.values.get('exp')
        response = DB.updateJobList(id,title,type,salary,postedDate,closedDate,status,description,exp);
    return response

if __name__ == '__main__':
   app.run()