from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'full_friends')

queries = {
    'create' : "INSERT INTO users (first_name, last_name, emails, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW());",
    'index' : "SELECT * FROM users",
    'edit': "SELECT * FROM users WHERE id = :id",
    'update':"UPDATE users \
            SET first_name = :first_name, last_name = :last_name, email = :email, \
            updated_at = NOW() \
            WHERE id = :id",
    'delete' : "DELETE FROM users WHERE id = :id"

}

@app.route('/')
def index():
    query = queries['index']
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = queries['index']
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
            }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
    query = queries['index']
    data = {
            'id': id
    }
    friend = mysql.query_db(query, data)
    return render_template('edit.html', friend=friend[0])

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = queries['update']
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'id': id
    }
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = queries['delete']
    data = {
            'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
