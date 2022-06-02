from flask import Flask
import secrets

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.secret_key = secrets.token_hex(16)
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '@Aa0174552687'
# app.config['MYSQL_DB'] = 'hiringSystem'
