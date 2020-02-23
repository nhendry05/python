from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'auddie'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = int(0)
    if 'activity' not in session:
        session['activity'] = []
    if 'try' not in session:
        session['try'] = int(0)
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['add_gold'] == 'farm':
        gold = random.randint(10,20)
        session['gold'] += gold
        session['try'] += 1
    elif request.form['add_gold'] == 'cave':
        gold = random.randint(5,10)
        session['gold'] += gold
        session['try'] += 1
    elif request.form['add_gold'] == 'house':
        gold = random.randint(2,5)
        session['gold'] += gold
        session['try'] += 1
    elif request.form['add_gold'] == 'casino':
        gold = random.randint(-50,50)
        session['gold'] += gold
        session['try'] += 1
    if gold >= 0:
        session['activity'].insert(0, ['Earned {} golds from the {}: {}'.format(gold, request.form['add_gold'], datetime.now()), True])
    if gold < 0:
        session['activity'].insert(0, ['Entered a casino and lost {} golds... Ouch..: {}'.format(abs(gold), datetime.now()), False])
    return redirect("/")

@app.route("/clear")
def logout():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)