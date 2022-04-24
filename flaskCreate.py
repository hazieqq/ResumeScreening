from flask import Flask, render_template, request, redirect, url_for, session,abort

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0