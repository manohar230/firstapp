from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
from datetime import datetime
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ="example"

mysql = MySQL(app)
@app.route('/')
def index():
    return render_template("index.html")