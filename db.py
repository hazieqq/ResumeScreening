from dataclasses import dataclass
from config import app
from flask_mysqldb import MySQL
import MySQLdb.cursors
mysql = MySQL(app)

class DB():

    def readProfile(session):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            session_convert = str(session)                                                          #covert id from int to string
            cursor.execute('SELECT * FROM accounts WHERE id = %s', (session_convert))
            data = cursor.fetchone()

            return data
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def readFromUser(username, password):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
            data = cursor.fetchone()

            return data
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def insertToUser(username, password, email, fullName, phoneNumber, country, currentCompany, uploadedfile):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)', (username, password, email, fullName, phoneNumber, country, currentCompany, uploadedfile))
            mysql.connection.commit()
            data = 'You have successfully registered!'
            return data
            
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def checkUserAccount(username):
        try:
            # Check if account exists using MySQL
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM accounts WHERE username = %s', (username))
            data = cursor.fetchone()

            return data
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def insertFile(file):
        try:
            print('insertintosuccess')
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO pdf_fille1 VALUES (%s)', ([file]))
            mysql.connection.commit()
            return 'success'
            
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def readFile():
        try:
            print('readfilesuccess')
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM pdf_fille1')
            data = cursor.fetchone()
            print(data)
            return data
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def uploadcv(id, session, filename, data):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            session_convert = str(session) 
            print('testuploadsuccess')
            cursor.execute('INSERT INTO user_cv VALUES (NULL, %s, %s, %s, %s)', (id, session_convert, filename, data))
            mysql.connection.commit()
            return 'success'
            
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def fetchtestupload(session):
        try:
            # print('fetch test upload success')
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            session_convert = str(session) 
            cursor.execute('SELECT * FROM user_cv where username="%s"' % (session_convert))
            data = cursor.fetchall()
            return data

        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def deletefile(id):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('DELETE FROM user_cv WHERE id = %s' % (id))
            mysql.connection.commit()
            return 'success'
            
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def updatefile(cv, data, id):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE user_cv SET cv=%s, data=%s WHERE id=%s', (cv, data, id))
            mysql.connection.commit()
            print('updatedsuccessfully')
            return 'success'
            
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def readalljob():
        try:
            print('readjobsuccess')
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM jobpost')
            data = cursor.fetchall()
            return data
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def readspecificjob(id):
        try:
            print('readspecificjobsuccess')
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM jobpost WHERE jobID = %s' % (id))
            data = cursor.fetchall()
            # print(data)
            return data
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def fetchapplyjobfiles(sessionid):
        try:
            print('readspecificjobfilesuccess')
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT cv FROM user_cv WHERE user_id = %s' % (sessionid))
            data = cursor.fetchall()
            # print(data)
            return data
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    def applyjob(session_id, jobapplyid):
        try:
            print('applyspecificjobfilesuccess')
            session_convert = str(session_id) 
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO applyjob VALUES (%s, %s, %s, %s, %s)', (session_convert, jobapplyid, 'active', jobapplyid, '9999-99-99'))
            mysql.connection.commit()
            return 'success'
        except Exception as e:
            print("Problem fetch from user table: " + str(e))
            return "fail"

    
