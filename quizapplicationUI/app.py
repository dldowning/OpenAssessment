import os

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = os.urandom(50)

app.config['MYSQL_HOST'] = 'mysqldatabase22.ckbrw4jjgoea.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'sqlmasteruser'
app.config['MYSQL_PASSWORD'] = 'T.srsdv123'
app.config['MYSQL_DB'] = 'Assessment'

mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'Email' in request.form and 'student_id' in request.form:
        Email = request.form['Email']
        student_id = request.form['student_id']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM User_Table WHERE Email = % s AND student_id = % s', (Email, student_id ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['Email']
            session['student_id'] = account['student_id']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'student_id' in request.form and 'First_Name' in request.form and 'Last_Name' in request.form and 'Email' in request.form and 'Degree' in request.form and 'Country' in request.form :
        #user_id = request.form['user_id']
        student_id = request.form['student_id']
        First_Name = request.form['First_Name']
        Last_Name = request.form['Last_Name']
        Email = request.form['Email']
        Degree = request.form['Degree']
        Country = request.form['Country']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM User_Table WHERE Email = % s', (Email,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', Email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', student_id):
            msg = 'name must contain only characters and numbers !'
        else:
            cursor.execute('INSERT INTO User_Table VALUES ( NULL, % s, % s, % s, % s, Now(), % s, % s)',
                          (student_id , First_Name, Last_Name, Email, Degree, Country))

            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)


@app.route("/index")
def index():
    if 'loggedin' in session:
         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
         cursor.execute('SELECT  course_number from Course_Table')
         joblist = cursor.fetchall()
         return render_template("index.html", joblist=joblist)


@app.route("/display")
def display():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM User_Table WHERE user_id = % s', (session['id'],))
        account = cursor.fetchone()
        return render_template("display.html", account=account)
    return redirect(url_for('login'))


@app.route("/update", methods=['GET', 'POST'])
def update():
    msg = ''
    if 'loggedin' in session:
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'address' in request.form and 'city' in request.form and 'country' in request.form and 'postalcode' in request.form and 'organisation' in request.form:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            organisation = request.form['organisation']
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            postalcode = request.form['postalcode']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM accounts WHERE username = % s', (username,))
            account = cursor.fetchone()
            if account:
                msg = 'Account already exists !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'name must contain only characters and numbers !'
            else:
                cursor.execute(
                    'UPDATE accounts SET username =% s, password =% s, email =% s, organisation =% s, address =% s, city =% s, state =% s, country =% s, postalcode =% s WHERE id =% s',
                    (username, password, email, organisation, address, city, state, country, postalcode,
                     (session['id'],),))
                mysql.connection.commit()
                msg = 'You have successfully updated !'
        elif request.method == 'POST':
            msg = 'Please fill out the form !'
        return render_template("update.html", msg=msg)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=int("5000"))
