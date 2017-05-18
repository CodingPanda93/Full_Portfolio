from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
#from time import strftime, gmtime
# ^ Uncomment this line after you verify the issue (Line: 57).
app = Flask(__name__)
app.secret_key= 'ThisIsASecret'


# ^ Try to group  your imports together at the top like so.  Also, if you're importing specifics, you can also import randint like so:  from random import randint

#Please use newlines to separate codes into logical groupings (I'll move around things in this project for you).  - N.T.

@app.route('/', methods= ['GET', 'POST'])
def index(): #Place a description comment here.  Ex: Adds gold to session if it doesn't exist, and displays main page.

    try:
        session['gold']
    except:
        session['gold'] = 0 #Watch your spacing here, try to keep things consistent (Note: this was session['gold']=0)

    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def gold(): #Needs description, see line 11.

    if request.form['building'] == 'farm':
        earning = random.randrange(10, 20)
        activity = 'Earned {} golds from the farm!'.format(earning)
        style = 'green'

    elif request.form['building'] == 'cave':
        earning = random.randrange(5, 10)
        activity = 'Earned {} golds from the cave!'.format(earning)
        style = 'green'

    elif request.form['building'] == 'house':
        earning = random.randrange(2, 5)
        activity = 'Earned {} golds from the house!'.format(earning)
        style = 'green'

    elif request.form['building'] == 'casino':
        earning = random.randrange(0, 51)
        gamble = random.randint(0,1)

        if gamble == 0: #No need to say == 0; 0 is falsey.  You can just say: if not earning:
            activity = 'Earned {} golds from the house!'.format(earning)
            style = 'green'
        else:
            activity = 'Lost {} golds from the casino..Ouch!'.format(earning)
            style = 'red'

	# ^ Good use of if/elif chains, good job recognizing the mutual exclusivity.

    session['gold'] += earning
    date = strftime("(%Y/%m/%d %I:%M %p)", gmtime()) #Did not import strftime or gmtime!!!!! CAUSES ERROR
    activity = activity + " " + date

    if 'activities' not in session:
        session['activities'] = []
    else:
        session['activities'].append([activity, style])

	# ^There's a problem on your template.  Your text doesn't stay within the div...Perhaps you should adjust the overflow-y within your css.

    return redirect('/')

#No reset function? :C
app.run(debug=True)
