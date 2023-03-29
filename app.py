import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://mutkus_lab_10_user:9JkJGkXZM0UhCs0ma5fpOGWJMDYwrxan@dpg-cgho5bg2qv2772n3qet0-a/mutkus_lab_10")
    conn.close()
    return "Database Connection Successful"