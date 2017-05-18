from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\.\+_-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app,'emaildb')
@app.route('/')
def index():
    query = 'SELECT * FROM friends'
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route('/success', methods=['POST'])
def create():
    if len(request.form['email']) > 1: #Validations for Emails
        flash('Email can not be empty!')

    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Email is not valid!')
    else:
        flash('The email address you entered (' + request.form['email'] + ') is a VALID email address! Thank you!' )
        query = 'INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())''
        # We'll then create a dictionary of data from the POST data received.
        data = {
                'email': request.form['email'],
                }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
