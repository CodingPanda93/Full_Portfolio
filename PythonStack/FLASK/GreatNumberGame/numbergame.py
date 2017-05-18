from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= 'ThisIsASecret'
import random

@app.route('/', methods= ['GET', 'POST'])
def random_num():
    flash = ''
    guess = int(request.form['guess'])
    if 'num' not in session:
        session['num']=random.randrange(0, 101) #sets num to be random integer if no num has been guessed
    elif guess < session['num']:
        flash = 'Too High!'
    elif guess > session['num']:
        flash = 'Too Low!'
    elif guess == session['num']:
        flash = str(guess) + 'was the number!'
    flash(message=flash, category='info')
    return render_template('index.html')
@app.route('/reset', methods = ['GET'])
def reset():
    session['num']=random.randrang(0,101)
    return redirect('/')
app.run(debug=True)
