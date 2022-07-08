from flask import Flask, render_template, request, redirect, url_for, session,abort, jsonify, send_file
import logging
from config import app
from db import DB
import urllib.request
from werkzeug.utils import secure_filename
import os
from io import BytesIO

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route("/index")
def index():
    data = DB.readalljob()
    if 'loggedin' in session:
        return render_template('index.html', check=1, name=session['username'], data=data)
    else:
        return render_template('index.html', check=2, data=data)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        fullName = request.form['fullName']
        phoneNumber = request.form['phoneNumber']
        country = request.form['country']
        currentCompany = request.form['currentCompany']

        data = DB.checkUserAccount(username)

        if data:
            msg = 'Account already exists!'
        else:
            data = DB.insertToUser(username, password, email, fullName, phoneNumber, country, currentCompany, uploadedfile)
            msg = 'You have successfully registered!'
            return redirect(url_for('login'))
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', check=2)

@app.route('/test', methods=['GET', 'POST'])
def test():
    msg = ''
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        print(username)
        print(password)
        account = DB.readFromUser(username, password)
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return 'success'
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', check=2) 

# @app.route("/test")
# def test():
#     if 'loggedin' in session:
#         return render_template('login.html', check=1, name=session['username'])
#     else:
#         return render_template('login.html', check=2)

@app.route("/joblisting")
def joblisting():
    data = DB.readalljob()
    print(type(data))
    if 'loggedin' in session:
        return render_template('job_listing.html', check=1, name=session['username'], data=data, sessionid=session['id'])
    else:
        return render_template('job_listing.html', check=2, data=data)

@app.route('/job_details/<int:id>')
def jobdetails(id):
    data = DB.readspecificjob(id)
    if 'loggedin' in session:
        files = DB.fetchapplyjobfiles(session['id'])
        print('jobdetails', files)
        return render_template('job_details.html', check=1, name=session['username'], data=data, files=files)
    else:
        return render_template('job_details.html', check=2, data=data)

@app.route('/about')
def about():
    if 'loggedin' in session:
        return render_template('about.html', check=1, name=session['username'])
    else:
        return render_template('about.html', check=2)

@app.route('/contact')
def contact():
    if 'loggedin' in session:
        return render_template('contact.html', check=1, name=session['username'])
    else:
        return render_template('contact.html', check=2)

@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return redirect(url_for('index'))

@app.route("/profile")
def profile():
    if 'loggedin' in session:
        fetch_upload = DB.fetchtestupload(session['username'])
        account = DB.readProfile(session['id'])
        return render_template('profile.html', account=account, data=fetch_upload, check=1)
    else:
        return redirect(url_for('test'))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     # check if the post request has the file part
#     if 'files[]' not in request.files:
#         resp = jsonify({'message' : 'No file part in the request'})
#         resp.status_code = 400
#         return resp
     
#     files = request.files.getlist('files[]')
#     # print(type(files))
#     # print(files)
#     errors = {}
#     success = False
#     pdf = ''
#     for file in files:
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             pdf += filename + ','
#             # DB.insertFile(filename)
#             # readfile = DB.readFile()
#             # result = secure_filename(str (readfile))
#             # file.save(os.path.join(app.config['UPLOAD_FOLDER'], result))
#             success = True
#         else:
#             errors[file.filename] = 'File type is not allowed'
    
#     new_pdf = pdf[:-1]
#     # print('new_pdf: '+new_pdf)
#     # print('success')
#     # DB.insertFile(new_pdf)

#     # retreve file from DB 
#     readfile = DB.readFile()
#     result = secure_filename(str (readfile))
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], result))
#     # print('result: '+result)
#     # print('result: '+new_result)

#     if success and errors:
#         errors['message'] = 'File(s) successfully uploaded'
#         resp = jsonify(errors)
#         resp.status_code = 206
#         return resp
#     if success:
#         resp = jsonify({'message' : 'Files successfully uploaded'})
#         resp.status_code = 201
#         return resp
#     else:
#         resp = jsonify(errors)
#         resp.status_code = 400
#         return resp

@app.route('/testupload', methods=['GET', 'POST'])
def testupload():
    if request.method == 'POST':
        files = request.files.getlist('file_name')
        print(files)

        for file in files:
            if file and allowed_file(file.filename):
                filename=file.filename
                data=file.read()
                DB.uploadcv(session['id'], session['username'], filename, data)
            else:
                return 'fail'
        return redirect(url_for('profilecv'))
    return render_template('index.html')

@app.route('/download')
def download():
    fetch_upload = DB.fetchtestdownload()
    print(fetch_upload)
    filename = fetch_upload['cv']
    data = fetch_upload['data']
    return send_file(BytesIO(data), attachment_filename=filename, as_attachment=True)

@app.route('/deletefile', methods=['POST'])
def deletefile():
    fileid = request.values.get('fileid')
    data = DB.deletefile(fileid)
    return data

@app.route('/updatefile/<int:id>', methods=['GET', 'POST'])
def updatefile(id):
    print('updatefile')

    if request.method == 'POST':
        files = request.files.getlist('file_name')
        print(files)
        for file in files:
            if file and allowed_file(file.filename):
                filename=file.filename
                data=file.read()
                print(filename)
                DB.updatefile(filename, data, id)
            else:
                return 'fail'
        return redirect(url_for('profilecv'))
    return render_template('index.html')

# @app.route('/updatefile', methods=['GET', 'POST'])
# def updatefile():
#     print('updatefile')

#     if request.method == 'POST':
#         id = request.values.get('fileid')
#         files = request.form['file_name']
#         files = request.form.get('file_name')
#         files = request.files['file_name']
#         print(id)
#         print(files)
#         for file in files:
#             if file and allowed_file(file.filename):
#                 filename=file.filename
#                 data=file.read()
#                 print(filename)
#                 DB.updatefile(filename, data, id)
#             else:
#                 return 'fail'
#         return redirect(url_for('profile'))
#     return render_template('index.html')

@app.route("/applyjob", methods=['GET', 'POST'])
def applyjob():
    jobid = request.values.get('id')
    jobtitle = request.values.get('title')
    print(' jobid', jobid)
    if 'loggedin' in session:
        data = DB.applyjob(session['id'], jobid, jobtitle)
        return data
    else:
        return redirect(url_for('test'))

@app.route('/profilepage')
def profilepage():
    if 'loggedin' in session:
        fetch_upload = DB.fetchtestupload(session['username'])
        account = DB.readProfile(session['id'])
        return render_template('profilepage.html', account=account, data=fetch_upload, check=1)
    else:
        return render_template('profilepage.html', check=2)

@app.route('/profilecv')
def profilecv():
    if 'loggedin' in session:
        fetch_upload = DB.fetchtestupload(session['username'])
        account = DB.readProfile(session['id'])
        return render_template('profilecv.html', account=account, data=fetch_upload, check=1)
    else:
        return render_template('profilecv.html', check=2)

@app.route('/appstatus')
def appstatus():
    if 'loggedin' in session:
        data = DB.displayapplyjob(session['id'])
        print(data)
        return render_template('appstatus.html', check=1, data=data)
    else:
        return render_template('appstatus.html', check=2)


if __name__ == "__main__":
    # db.create_all
    app.run(debug=True)
