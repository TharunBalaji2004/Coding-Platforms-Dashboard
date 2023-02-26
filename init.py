from flask import Flask, redirect, render_template, request, url_for, session
import mysql.connector
import os

mydb = mysql.connector.connect(host="localhost",user="placementadmin", passwd="citchennai",database="CodingDashboard",auth_plugin="mysql_native_password")
cursor = mydb.cursor()

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def home():
    return render_template("redirect.html")

@app.route('/login', methods=['post','get'])
def login():
    return render_template("index.html")

@app.route('/stafflogin', methods=['post','get'])
def stafflogin():
    error = None
    if (request.method == 'POST'):
        uname = request.form.get('username')
        password = request.form.get('password')
        if (len(uname)==0 or len(password)==0):
            error = "Username or Password is empty"
        else:
            query = "SELECT * FROM STAFF WHERE USERNAME = %s AND PASSWORD = %s"
            cursor.execute(query, (uname,password))
            rows = cursor.fetchall()
            countrows = cursor.rowcount
            if (countrows < 1):
                error = "Invalid Login Details"
            else:
                session["username"] = uname
                error = None
                return redirect(url_for("dashboard"))

    return render_template('index.html',error = error) 

@app.route('/dashboard')
def dashboard():
    uname = session.get("username")
    if (uname is None):
        return redirect(url_for("login"))

    return render_template("dashboard.html",username=uname)

@app.route('/logout')
def logout():
    session.pop("username",None)
    return redirect(url_for("login"))

@app.route('/codechef', methods=['post','get'])
def codechef():
    query = "SELECT * FROM CSEC_CC;"
    cursor.execute(query)
    results = cursor.fetchall()
    table_head = ["Rating","Div","Star"]
    return render_template("dashboard.html",results=results,table_head=table_head,n=len(table_head))

@app.route('/leetcode', methods=['post','get'])
def leetcode():
    query = "SELECT * FROM CSEC_LC;"
    cursor.execute(query)
    results = cursor.fetchall()
    table_head = ["Solved","Easy","Medium","Hard","Rating"]
    return render_template("dashboard.html",results=results,table_head=table_head,n=len(table_head))

@app.route('/hackerrank', methods=['post','get'])
def hackerrank():
    query = "SELECT * FROM CSEC_HR;"
    cursor.execute(query)
    results = cursor.fetchall()
    table_head = ["Badges Count","Python","C","C++","Java","SQL","Problem Solving"]
    return render_template("dashboard.html",results=results,table_head=table_head,n=len(table_head))

@app.route('/geeksforgeeks', methods=['post','get'])
def geeksforgeeks():
    query = "SELECT * FROM CSEC_GFG;"
    cursor.execute(query)
    results = cursor.fetchall()
    table_head = ["Solved","School","Basic","Easy","Medium","Hard"]
    return render_template("dashboard.html",results=results,table_head=table_head,n=len(table_head))

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

if __name__ == "__main__":
    app.run(debug = True)