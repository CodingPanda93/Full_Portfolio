from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\.\+_-]+\.[a-zA-Z]*$')
PASSWORDregex = re.compile(r'^(?=[^A-Z]*[A-Z])(?=[^0-9]*[0-9])[\w\d]{8,}$')
DATEregex = re.compile(r'([0-1][0-9])\/([0-3][0-9])\/([1-9][0-9][0-9][0-9])')

'''This does not run. Indentation error on line 71.  As well as an isalpha error on line 33.  Please use this opportunity to practice separating your code into logical blocks that do similar things (See the last assignment: Ninja Gold).  - N.T.

'''

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/form')
def register():
    return render_template('register.html')
@app.route('/validate', methods=['POST'])
def validate():
    if len(request.form['fname']) < 1: #Validations for First Name
        flash('First Name can not be empty!')

    elif not request.form['fname'].isalpha(): #Nice use of isalpha.
        flash('First Name can not contain any numbers or special characters!')

    else:
        fname = request.form['fname']

    if len(request.form['lname']) < 1: #Validations for Last Name
        flash('Last Name can not be empty!')

    elif isalpha(request.form['lname']) == False: #This will not work.  isalpha() is a method pertaining to a string, it is not a built-in standalone function (See: Line 24).
        flash('Last Name can not contain any numbers or special characters!')

    else:
        comment= request.form['lname'] #Keep your spacing consistent.

    if len(request.form['email']) > 1: #Validations for Emails
        flash('Email can not be empty!')

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")

    else:
        email = request.form['email']

    password = request.form['password']

    if len(password) < 1: #Validations for Password
        flash('Password can not be empty!')

    elif not PASSWORDregex.match(password):
        flash('Password needs to be more than 8 characters!')

    elif password != request.form['confirm']:
        flash('Your passwords do not match')

    else:
        comment= request.form['password']

    if len(request.form['confirm']) < 1: #Validations for Confirm Password
        flash('You must confirm your password')
        return redirect('/')
    elif request.form['confirm'] == request.form['password']:
        flash('Your confirmation does not match your password')
        return redirect('/')
    else:
        comment= request.form['lname']

    date_valid = DATEregex.match(request.form['birth_date'])# Validations date
    today = date.today()
    if not date_valid:
            flash('Please enter your birthdate in the format: MM/DD/YYYY')
        else: #Indentation error, I think this is supposed to be tabbed back one.
            birth_date = date(int(birth_date_valid.group(3)), int(birth_date_valid.group(1)), int(birth_date_valid.group(1)))
            if not birth_date < today: #What happens if your user is 500000 years old?
                flash("Date enter is not valid")
    return redirect('/')
app.run(debug=True)
