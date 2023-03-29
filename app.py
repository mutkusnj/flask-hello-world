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

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://mutkus_lab_10_user:9JkJGkXZM0UhCs0ma5fpOGWJMDYwrxan@dpg-cgho5bg2qv2772n3qet0-a/mutkus_lab_10")
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    
    conn.commit()
    conn.close()
    
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://mutkus_lab_10_user:9JkJGkXZM0UhCs0ma5fpOGWJMDYwrxan@dpg-cgho5bg2qv2772n3qet0-a/mutkus_lab_10")
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    
    conn.commit()
    conn.close()
    
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://mutkus_lab_10_user:9JkJGkXZM0UhCs0ma5fpOGWJMDYwrxan@dpg-cgho5bg2qv2772n3qet0-a/mutkus_lab_10")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM Basketball;")
    records = cur.fetchall()
    
    conn.close()
    
    response = "<table>"
    
    for player in records:
        response = response + "<tr>"
        
        for player_data in player:
            response = response + "<td>{}</td>".format(player_data)
            
        response = response + "<tr>"
        
    response = response + "</table>"
    
    return response

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://mutkus_lab_10_user:9JkJGkXZM0UhCs0ma5fpOGWJMDYwrxan@dpg-cgho5bg2qv2772n3qet0-a/mutkus_lab_10")
    cur = conn.cursor()
    
    cur.execute("DROP TABLE Basketball;")
    
    conn.commit()
    conn.close()
    
    return "Basketball Table Successfully Dropped"