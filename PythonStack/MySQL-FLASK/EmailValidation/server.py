from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\.\+_-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app,'emaildb')

queries = {
    'create' : "INSERT INTO emails (email, created_at) VALUES (:email, NOW(), NOW());",
    'index' : "SELECT * FROM emails",
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if(validateEmail(request.form['email'])):
            query = queries['create']
            data = {
                    'email': request.form['email'],
                    }
            flash('The email address you entered (' + request.form['email'] + ') is a VALID email address! Thank you!')
            return redirect('/success')
        else:
            flash('Email is not valid!')
    return render_template('index.html')
@app.route('/success', methods=['GET'])
def success():
        query = queries['index']
        data = {}
        emails = mysql.query_db(query, data)
        return render_template('success.html', emails=emails)
def validateEmail(email):
    # Return whether or not the email passed in is valid
    return EMAIL_REGEX.match(email)

app.run(debug=True)
