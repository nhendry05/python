from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = "jamesy"
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
pass_valid = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%&*?^])[a-zA-z0-9!@#$%&*?^]+$')
@app.route("/")
def register():
    return render_template('index.html')

@app.route("/add_user", methods = ["POST"])
def add_new_to_db():
    is_valid = True
    if len(request.form['fname']) <1:
        is_valid = False
        flash("Please Enter First Name")
    if re.findall("[^a-zA-Z]", request.form['fname']):
        is_valid = False
        flash("First Name must consist of only letters")
    if len(request.form['lname']) <1:
        is_valid = False
        flash("Please Enter Last Name")
    if re.findall("[^a-zA-Z]", request.form['lname']):
        is_valid = False
        flash("Last Name must consist of only letters")
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Invalid email address")
    if len(request.form['pw']) <5:
        is_valid = False
        flash("Password must be at least 5 characters")
    if request.form['pw'] != request.form['cpw']:
        is_valid = False
        flash("Passwords must match")
    if not re.search(pass_valid, request.form['pw']):
        is_valid = False
        flash("Password is invalid")
    if is_valid:
        pw_hash = bcrypt.generate_password_hash(request.form['pw'])
        print(pw_hash)
        mysql = connectToMySQL("registration")
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, %(password_hash)s, NOW(), NOW())"
        data = {
            'fn': request.form['fname'],
            'ln': request.form['lname'],
            'em': request.form['email'],
            'password_hash': pw_hash
        }
        results = mysql.query_db(query, data)
        flash("User Added Successfully")
    return redirect("/")

@app.route("/login", methods = ["POST"])
def login():
    is_valid = True
    if len(request.form['email']) < 1:
        is_valid = False
    if is_valid:
        mysql = connectToMySQL("registration")
        query = "SELECT * FROM users WHERE email = %(em)s;"
        data = {
            "em": request.form["email"]
        }
        result = mysql.query_db(query, data)
        if result:
            user_data = result[0]
            if bcrypt.check_password_hash(user_data['password'], request.form['pw']):
                session['user_id'] = user_data['id_user']
                return redirect("/tweets")
            else:
                is_valid = False
        else:
            is_valid = False
    if not is_valid:
        flash("Invalid email or password")
        return redirect("/")

@app.route("/tweets")
def success():
    if 'user_id' not in session:
        return redirect("/")

    mysql = connectToMySQL('registration')
    query = "SELECT * FROM users WHERE id_user = %(id)s"
    data = {
        'id' : session['user_id']
    }
    result = mysql.query_db(query, data)
    if result:
        user_data = result[0]
    
    mysql = connectToMySQL('registration')
    query = "SELECT users.first_name, users.last_name, tweets.content, tweets.created_at FROM tweets JOIN users ON tweets.author = users.id_user ORDER BY tweets.created_at DESC"
    all_tweets = mysql.query_db(query)
    print(all_tweets)
    #NEW STUFF BETWEEN
    now = datetime.now()
    print(now)
    #

    return render_template("login.html", user_data=user_data, all_tweets=all_tweets, now=now)

@app.route("/add_tweet", methods = ["POST"])
def add_tweet():
    is_valid = True
    if len(request.form['tweet_content']) < 1:
        is_valid = False
        flash("Tweet content must not be blank")
    if len(request.form['tweet_content']) >255:
        is_valid = False
        flash("Tweet content must be less than 255 characters")
    if is_valid:
        mysql = connectToMySQL("registration")
        query = "INSERT INTO tweets (content, author, created_at, updated_at) VALUES (%(cont)s, %(author_id)s, NOW(), NOW())"
        data = {
            'cont' : request.form['tweet_content'],
            'author_id': session['user_id']
        }
        mysql.query_db(query, data)
        flash("Tweet Added Successfully")
    return redirect("/tweets")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)