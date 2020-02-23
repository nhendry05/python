from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = "jamesy"

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
    if len(request.form['pw']) <5:
        is_valid = False
        flash("Password must be at least 5 characters")
    if request.form['pw'] != request.form['cpw']:
        is_valid = False
        flash("Passwords must match")
    if is_valid:
        mysql = connectToMySQL("registration")
        query = "INSERT INTO users (first_name, last_name, password, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(pw)s, NOW(), NOW())"
        data = {
            'fn': request.form['fname'],
            'ln': request.form['lname'],
            'pw': request.form['pw']
        }
        user_id = mysql.query_db(query, data)
        flash("User Added Successfully")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)