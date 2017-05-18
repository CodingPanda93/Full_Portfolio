from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= 'ThisIsASecret'

@app.route('/')
def counter():
   try:
       session['counter']
   except:
       session['counter']=0
   session['counter']+=1
   return render_template('index.html')
@app.route('/ninjas', methods=['POST'])
def ninjas():
   session['counter']+=1
   return redirect('/')
@app.route('/hackers', methods=['POST'])
def hackers():
    session['counter']=0
    return redirect('/')
app.run(debug=True) # run our server
