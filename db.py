from flaskCreate import app
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL(app)


class DB():
    
    def insertIntoJobPost(title,category,jobtype,vacancy,experience,date,salaryFrom,qualification,description,status1):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO jobpost VALUES (NULL, % s, % s, % s,% s,% s,% s,% s,% s,% s)', (title,jobtype,description,qualification,category,date,salaryFrom,status1,experience,))
            mysql.connection.commit()
            return "success"
        except Exception as e:
            print("Problem inserting into db: " + str(e))
            return "fail"
        
    def readFromJobApply():
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM jobapply')
            data = cursor.fetchall()
            return data
        except Exception as e:
            print("Problem fetch from jobapply table: " + str(e))
            return "fail"
    
    def readFromUserAccount(userID):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM user_account where userID=%s' % (userID))
            data = cursor.fetchall()
            return data
        except Exception as e:
            print("Problem fetch from jobapply table: " + str(e))
            return "fail"
        
    def deleteJobApply(jobApplyID):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('DELETE FROM jobapply where jobapplyID=%s' % (jobApplyID))
            mysql.connection.commit()
            return "success"
        except Exception as e:
            print("Problem deleting from jobapply table: " + str(e))
            return "fail"
        
    def updateJobApply(jobApplyID,text):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE jobapply SET applicantStatus = %s WHERE jobapplyID=%s',(text,jobApplyID))
            mysql.connection.commit()
            return "success"
        except Exception as e:
            print("Problem updating into jobapply table: " + str(e))
            return "fail"