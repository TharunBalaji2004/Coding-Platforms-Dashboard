from flask import Flask, redirect, render_template, request, url_for, session
import mysql.connector

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
    section = "GENERAL LEADERBOARD"
    return render_template("dashboard.html",username=uname,section=section)

@app.route('/general')
def general():
    section = "GENERAL LEADERBOARD"
    return render_template("dashboard.html",section=section)

@app.route('/csea')
def csea():
    section = "CSE A LEADERBOARD"
    return render_template("dashboard.html",section=section)

@app.route('/cseb')
def cseb():
    section = "CSE B LEADERBOARD"
    return render_template("dashboard.html",section = section)

@app.route('/csec')
def csec():
    section = "CSE C LEADERBOARD"
    
    return render_template("dashboard.html",section = section)

@app.route('/codechef', methods=['post','get'])
def codechef():
    temp = list(request.form.to_dict().keys())
    section = temp[0]
    class_name = ""

    if ("CSE A" in section): class_name = "CSEA"
    if ("CSE B" in section): class_name = "CSEB"
    if ("CSE C" in section): class_name = "CSEC"
    query = "SELECT * FROM {0}_CC;".format(class_name)
    table_head = ["Rating","Div","Star"]

    if ("GENERAL" in section):
        query = "SELECT * FROM CSE_GENERAL_CC ORDER BY RATING DESC"
        table_head = ["Class","Rating","Div","Star"]

    
    cursor.execute(query)
    results = cursor.fetchall()
    
    return render_template("dashboard.html",results=results,table_head=table_head,section=section)

@app.route('/leetcode', methods=['post','get'])
def leetcode():
    temp = list(request.form.to_dict().keys())
    section = temp[0]
    class_name = ""

    if ("CSE A" in section): class_name = "CSEA"
    if ("CSE B" in section): class_name = "CSEB"
    if ("CSE C" in section): class_name = "CSEC"
    query = "SELECT * FROM {0}_LC;".format(class_name)
    table_head = ["Solved","Easy","Medium","Hard","Rating"]

    if ("GENERAL" in section):
        query = "SELECT * FROM CSE_GENERAL_LC ORDER BY RATING DESC"
        table_head = ["Class","Solved","Easy","Medium","Hard","Rating"]
        
    cursor.execute(query)
    results = cursor.fetchall()
    
    return render_template("dashboard.html",results=results,table_head=table_head,section=section)

@app.route('/hackerrank', methods=['post','get'])
def hackerrank():
    temp = list(request.form.to_dict().keys())
    section = temp[0]
    class_name = ""

    if ("CSE A" in section): class_name = "CSEA"
    if ("CSE B" in section): class_name = "CSEB"
    if ("CSE C" in section): class_name = "CSEC"
    query = "SELECT * FROM {0}_HR;".format(class_name)
    table_head = ["Badges Count","Python","C","C++","Java","SQL","Problem Solving"]

    if ("GENERAL" in section):
        query = "SELECT * FROM CSE_GENERAL_HR"
        table_head = ["Class","Badges Count","Python","C","C++","Java","SQL","Problem Solving"]

    cursor.execute(query)
    results = cursor.fetchall()   
    return render_template("dashboard.html",results=results,table_head=table_head,section=section)

@app.route('/geeksforgeeks', methods=['post','get'])
def geeksforgeeks():
    temp = list(request.form.to_dict().keys())
    section = temp[0]
    class_name = ""
    
    if ("CSE A" in section): class_name = "CSEA"
    if ("CSE B" in section): class_name = "CSEB"
    if ("CSE C" in section): class_name = "CSEC"
    query = "SELECT * FROM {0}_GFG;".format(class_name)
    table_head = ["Solved","School","Basic","Easy","Medium","Hard"]

    if ("GENERAL" in section):
        query = "SELECT * FROM CSE_GENERAL_GFG ORDER BY SOLVED DESC"
        table_head = ["Class","Solved","School","Basic","Easy","Medium","Hard"]
        
    cursor.execute(query)
    results = cursor.fetchall()  
    return render_template("dashboard.html",results=results,table_head=table_head,section=section)

@app.route('/logout')
def logout():
    session.pop("username",None)
    return redirect(url_for("login"))

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

if __name__ == "__main__":
    app.run(debug = True)