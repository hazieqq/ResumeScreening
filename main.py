from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import MySQLdb.cursors
import re
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rusyaididatabase'
app.config['MYSQL_DB'] = 'pythonlogin'

mysql = MySQL(app)

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('index'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)

@app.route("/index")
def index():
    if 'loggedin' in session:
        return render_template('index.html', check=1, name=session['username'])
    else:
        return render_template('index.html', check=2)
    
@app.route("/joblisting")
def joblisting():
    if 'loggedin' in session:
        return render_template('job_listing.html', check=1, name=session['username'])
    else:
        return render_template('job_listing.html', check=2)

@app.route("/profile")
def profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        return render_template('profile.html', account=account, check=1)
    return redirect(url_for('login'))

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

@app.route('/job_details')
def job_details():
    if 'loggedin' in session:
        return render_template('job_details.html', check=1, name=session['username'])
    else:
        return render_template('job_details.html', check=2)

# @app.route('/login')
# def login():
#     return render_template('login.html')

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

        f = request.files['file']
        #create dir
        # dir_name = "D:/Final Year Project/New folder/ResumeScreening/static/files/" + username + "/"
        # os.mkdir(dir_name)
        # app.config["UPLOAD_PATH"] =  dir_name
        # f.save(os.path.join(app.config["UPLOAD_PATH"], f.filename))
        # dir_name_update = "D:/Final Year Project/New folder/ResumeScreening/static/files/" + username + "/" +f.filename
        # uploadedfile = convertToBinaryData(dir_name_update);

        # sql_insert = """ INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)"""
        # values = (username, password, email, fullName, phoneNumber, country, currentCompany, uploadedfile)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:

            # cursor.execute(sql_insert, values)
            # mysql.connection.commit()
            path = "D:\Test\8k.pdf"
            sql_fetch_blob_query = """SELECT * from accounts where id = %s"""
            value=(17,)
            cursor.execute(sql_fetch_blob_query, (value,))
            record = cursor.fetchall()
            for row in record:
                file = row[8]
                write_file(file, path)
            #create dir
            # dir_name = "D:/Final Year Project/New folder/ResumeScreening/static/files/" + username + "/"
            # os.mkdir(dir_name)
            # app.config["UPLOAD_PATH"] =  dir_name
            # f.save(os.path.join(app.config["UPLOAD_PATH"], f.filename))

            msg = 'You have successfully registered!'
            return redirect(url_for('login'))
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)

@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == "__main__":
    # db.create_all
    app.run(debug=True)