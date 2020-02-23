from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/users")
def all_users():
    query = "SELECT * FROM friends"
    mysql = connectToMySQL('users')
    all_users = mysql.query_db(query)
    print(all_users)
    return render_template("index.html", all_friends = all_users)

@app.route("/users/new")
def new():
    return render_template("new_user.html")

@app.route("/users/create", methods = ["POST"])
def add_new_user_to_db():
    mysql = connectToMySQL("users")
    query = "INSERT INTO friends (first_name, last_name, email, description, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, %(ds)s, NOW(), NOW())"
    data = {
        'fn': request.form['fname'],
        'ln': request.form['lname'],
        'em': request.form['email'],
        'ds': request.form['desc']
    }
    user_id = mysql.query_db(query, data)
    return redirect('/users/{}'.format(user_id))

@app.route("/users/<user_id>")
def show(user_id):
    mysql = connectToMySQL('users')
    query = "SELECT * FROM friends WHERE friend_id = %(id)s"
    data = {
        'id': user_id
    }
    user = mysql.query_db(query, data)
    print(user)
    return render_template("user_info.html", user = user[0])

@app.route("/users/edit/<user_id>")
def edit(user_id):
    mysql = connectToMySQL("users")
    query = "SELECT * FROM friends WHERE friend_id = %(id)s"
    data = {
        'id': user_id
    }
    user = mysql.query_db(query, data)
    print(user)
    return render_template("user_edit.html", user = user[0])

@app.route("/users/update/<user_id>", methods = ['POST'])
def update(user_id):
    query = "UPDATE friends SET first_name=%(fn)s, last_name=%(ln)s, email=%(em)s, description=%(ds)s, updated_at=NOW() WHERE friend_id = %(id)s"
    data = {
        'fn': request.form['fname'],
        'ln': request.form['lname'],
        'em': request.form['email'],
        'ds': request.form['desc'],
        'id': user_id
    }
    mysql = connectToMySQL("users")
    mysql.query_db(query,data)
    return redirect('/users/{}'.format(user_id))

@app.route("/users/destroy/<user_id>")
def delete(user_id):
    query = "DELETE FROM friends WHERE friend_id = %(id)s"
    data = {
        'id': user_id
    }
    mysql = connectToMySQL('users')
    user = mysql.query_db(query, data)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)