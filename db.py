from flaskCreate import app
from flask_mysqldb import MySQL
import MySQLdb.cursors
mysql = MySQL(app)


class DB():
    
    def insertIntoJobPost(title,jobtype,experience,closedDate,postedDate,salaryFrom,description,status1):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO jobpost VALUES (NULL, % s, % s, % s,% s,% s,% s,% s,% s)', (title,jobtype,description,closedDate,postedDate,salaryFrom,status1,experience))
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
        
    def readFromJobPost():
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM jobpost')
            data = cursor.fetchall()
            return data
        except Exception as e:
            print("Problem fetch from jobpost table: " + str(e))
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
        
    def deleteJobList(jobpostid):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('DELETE FROM jobpost where jobpostID=%s' % (jobpostid))
            mysql.connection.commit()
            return "success"
        except Exception as e:
            print("Problem deleting from jobpost table: " + str(e))
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
        
    def updateJobList(id,title,type,salary,postedDate,closedDate,status,description,exp):
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE jobpost SET title = %s, jobtype = %s, salaryFrom = %s,  postedDate = %s, closeddate = %s, status1 = %s,description=%s,experience=%s  WHERE jobpostID=%s',(title,type,salary,postedDate,closedDate,status,description,exp,id))
            mysql.connection.commit()
            return "success"
        except Exception as e:
            print("Problem updating into jobPost table: " + str(e))
            return "fail"