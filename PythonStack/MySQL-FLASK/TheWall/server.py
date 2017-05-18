from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'the_wall')
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import strftime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\.\+_-]+\.[a-zA-Z]*$')
PASSWORDregex = re.compile(r'^(?=[^A-Z]*[A-Z])(?=[^0-9]*[0-9])[\w\d]{8,}$')

#Holds all queries to use throughout page
queries = {
    #creates all new users into database
    'create_user' : "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())",
    #for selection of all users within database (not currently in use for this site)
    'index' : "SELECT * FROM users",
    #validate email within database
    'validate': "SELECT * FROM users WHERE email = :email"
    #display all messages onto the page
    'display_messages': "SELECT messages.id AS id, CONCAT(users.first_name, " ", users.last_name) AS username, messages.message, DATE_FORMAT(messages.created_at, '%M %D %Y') AS posted_date\
                        FROM messages\
                        JOIN users ON users.id = messages.user_id\
                        ORDER BY messages.created_at DESC"
    #displays all comments onto the page
    'display_comments': "SELECT comments.id AS id, comments.messages_id, CONCAT(users.first_name, " ", users.last_name) AS username, comments.comment, DATE_FORMAT(comments.created_at, '%M %D %Y') AS posted_date \
                        FROM comments\
                        JOIN users ON users.id = comments.user_id\
                        ORDER by comments.created_at ASC"
    'post_message': "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :user_id)"
    'post_comment': "INSERT INTO comments (comment, created_at, updated_at, user_id, messages_id) VALUES (:comment, NOW(), NOW(), :user_id, messages_id)"
    }

#displays registration and login pages
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#Registration form with validation and encrypting
@app.route('/register', methods=['POST'])
def create():
    #verification variable
    error = False
    if len(request.form['first_name']) < 1: #Validations for First Name
        flash('First Name can not be empty!')
        error = True

    elif not request.form['first_name'].isalpha():
        flash('First Name can not contain any numbers or special characters!')
        error = True

    if len(request.form['last_name']) < 1: #Validations for Last Name
        flash('Last Name can not be empty!')
        error = True

    elif not (request.form['last_name']).isalpha():
        flash('Last Name can not contain any numbers or special characters!')
        error = True

    if len(request.form['email']) < 1: #Validations for Emails
        flash('Email can not be empty!')
        error = True

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        error = True

    if len(request.form['password']) < 1: #Validations for Password
        flash('Password can not be empty!')
        error = True

    elif PASSWORDregex.match(request.form['password']):
        flash('Password needs to be more than 8 characters!')
        error = True

    elif request.form['password'] != request.form['confirm']:
        flash('Your passwords do not match')
        error = True

    if len(request.form['confirm']) < 1: #Validations for Confirm Password
        flash('You must confirm your password!')
        error = True

        #Validation Statements: IF error holds a value it will return back to the main page and display flash messaging,
        # ELSE the information will be encrypted and saved to database

    if error:
        return redirect('/')

    else:
        # PASSED ALL VALIDATIONS: creating the password hash with bcrypt and earlier made variables
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        query = queries['create_user']
        data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'password': pw_hash
        }
        mysql.query_db(query, data)
        # stores in session for wall page
        session['user'] = {
                'first_name': data['first_name'],
        }
        return render_template('wall.html')

@app.route ('/login', methods=['POST'])
def login():
    data = {
            'email': request.form['email'],
            'password': request.form['password']
    }
    query = queries['validate']
    user = mysql.query_db(query, data)
    #validates login with password in database
    if not user or not bcrypt.check_password_hash(user[0]['password'], data['password']):
        flash("Invalid email or password!")
        return redirect('/')
    else:
        # stores in session for wall page
        session['user'] = {
                'id': user[0]['id'],
                'first_name': user[0]['first_name'],
                'last_name': user[0]['last_name'],
        }
        return render_template('wall.html')

# remove session 'user' information and returns to main page
@app.route('/logout')
def logout():
    del session['user']
    return redirect('/')

# displays all messages and comments onto the wall page on log on
@app.route('/wall' methods=['GET'])
def display_wall():
    query = queries['display_messages']
    messages = mysql.query_db(query)
    query = queries['display_comments']
    comments = mysql.querry_db(query)
    return render_template('wall.html', messages=messages, comments=comments)

#add message to database and stores user information in sessions
@app.route('/message' methods=['POST'])
def post_message():
    query = queries['post_message']
    data = {
                'user_id': session['user']['id'],
                'message': request.form['message']
        }
        mysql.query_db(query, data)
    return redirect('/wall')

#add comment to database and stores user information in sessions
@app.route('/comment' methods=['POST'])
def post_comment():
    query = queries['post_comment']
    data = {
                'user_id': session['user']['id'],
                'message_id': int(request.form['message_id']),
                'comment': requestion.form['comment']
        }
        mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)
