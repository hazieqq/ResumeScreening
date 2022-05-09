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
    