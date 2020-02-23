from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/', methods = ['GET','POST'])
def index():
    session['number'] = random.randint(1,100)
    print(session['number'])
    return render_template("index.html")

@app.route('/guess', methods =['POST'])
def guess():
    if int(request.form['guess']) == session['number']:
        print("correct")
        return render_template("index.html", answer_on_template = "correct!")
    elif int(request.form['guess']) < session['number']:
        print("guess is too low")
        return render_template("index.html", answer_on_template = "Too Low!")
    elif int(request.form['guess']) > session['number']:
        print("guess is too high")
        return render_template("index.html", answer_on_template = "Too high!")


if __name__=="__main__":
    app.run(debug=True)