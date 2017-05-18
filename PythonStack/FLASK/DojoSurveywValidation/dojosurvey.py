from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1:
        flash('Name can not be empty!')
        return redirect('/')
    else:
        name = request.form['name']
    if len(request.form['comment']) < 1:
        flash('Comment section can not be empty!')
        return redirect('/')
    else:
        comment= request.form['comment']
    if len(request.form['comment']) > 120:
        flash('You can not have more than 120 characters within this section.')
        return redirect('/')
    else:
        location = request.form['location']
        language = request.form['language']
        return render_template("result.html", name=name, location=location, language=language, comment=comment)
app.run(debug=True) # run our server
