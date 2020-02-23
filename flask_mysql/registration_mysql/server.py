from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = "jamesy"

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
        flash("Invalid email address!")
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
        mysql = connectToMySQL("registration")
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, %(pw)s, NOW(), NOW())"
        data = {
            'fn': request.form['fname'],
            'ln': request.form['lname'],
            'em': request.form['email'],
            'pw': request.form['pw']
        }
        user_id = mysql.query_db(query, data)
        flash("User Added Successfully")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)