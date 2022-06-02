from flask import Flask
import secrets

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.secret_key = secrets.token_hex(16)
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '@Aa0174552687'
# app.config['MYSQL_DB'] = 'hiringSystem'


app.config['MYSQL_HOST'] = 'us-cdbr-east-05.cleardb.net'
app.config['MYSQL_USER'] = 'bf95b08e3361d6'
app.config['MYSQL_PASSWORD'] = 'bbac4a3f'
app.config['MYSQL_DB'] = 'heroku_c7805820ef04b71'