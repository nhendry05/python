from flask import Flask, render_template, redirect, request, session, flash, url_for
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "jamesy"
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
pass_valid = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%&*?^])[a-zA-z0-9!@#$%&*?^]+$')

#returns template for login page
@app.route("/")
def main():
    return render_template("login.html")

#registers user
@app.route("/register", methods = ['POST'])
def register():
    #validating user registration
    is_valid = True
    if len(request.form['fname']) < 1:
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
        flash("invalid email address")
    if len(request.form['pw']) < 5:
        is_valid = False
        flash("Password must be at least 5 characters")
    if request.form['pw'] != request.form['cpw']:
        is_valid = False
        flash("Passwords must match")
    if not re.search(pass_valid, request.form['pw']):
        is_valid = False
        flash("Password is invalid")
    if not is_valid:
        #if it isnt valid, return to login/registration page and display flash messages
        return redirect("/")
    else:
    #if all validations pass
    #insert that information into the users database
        pw_hash = bcrypt.generate_password_hash(request.form['pw'])
        mysql = connectToMySQL("enhanced_wall")
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, %(password_hash)s, NOW(), NOW())"
        data = {
            'fn': request.form['fname'],
            'ln': request.form['lname'],
            'em': request.form['email'],
            'password_hash': pw_hash
        }
        results = mysql.query_db(query, data)
        #after inserting into database, select from database to login
        mysql = connectToMySQL('enhanced_wall')
        query = "SELECT * FROM users WHERE email = %(em)s"
        data = {
            'em': request.form['email']
        }
        result = mysql.query_db(query, data)
        #if email was found in the database
        if result:
            user_data = result[0]
            session['user_id'] = user_data['user_id']
        #return to the landing page
        return redirect("/landing")

#logs user in
@app.route("/login", methods = ['POST'])
def login():
    is_valid = True
    #checks to make sure email is entered
    if len(request.form['email']) < 1:
        is_valid = False
    #if email is entered, continue
    if is_valid:
        mysql = connectToMySQL('enhanced_wall')
        query = "SELECT * FROM users WHERE email = %(em)s"
        data = {
            'em': request.form['email']
        }
        result = mysql.query_db(query, data)
        #if email was found in the database
        if result:
            user_data = result[0]
            #check to see if the password is correct
            if bcrypt.check_password_hash(user_data['password'], request.form['pw']):
                #opens a session with user_id and returns to landing page
                session['user_id'] = user_data['user_id']
                return redirect("/landing")
            else: #if the pasword doesnt match
                is_valid = False
        else: #if the email is not in the database
            is_valid = False
    if not is_valid: #if email is not in database or password is incorrect, return back to login/registration page
        flash("Invalid email or password")
        return redirect("/")

#user is brought here if login is successful
@app.route("/landing")
def landing():
    #if user is not logged in, return to login page
    if 'user_id' not in session:
        return redirect("/")
    #if user is logged in, retrieve user information for specific user session
    mysql = connectToMySQL('enhanced_wall')
    query = "SELECT * FROM users WHERE user_id = %(id)s"
    data = {
        'id': session['user_id']
    }
    result = mysql.query_db(query, data)
    print(result)
    if result: #if a user exists with that user_id, select the first user in the user table (should only be one)
        user_data = result[0]

    #join user to their messages to display in table, newest first
    mysql = connectToMySQL('enhanced_wall')
    query = "SELECT users.user_id, users.first_name, users.last_name, messages.message_id, messages.content, messages.author, messages.created_at FROM messages JOIN users ON messages.author = users.user_id ORDER BY messages.created_at DESC"
    all_messages = mysql.query_db(query)

    #count all the likes
    mysql = connectToMySQL('enhanced_wall')
    query = "SELECT message_like, COUNT(message_like) AS like_count FROM likes GROUP BY message_like"
    like_count = mysql.query_db(query)
    
    for message in all_messages:
        for like in like_count:
            if like['message_like'] == message['message_id']:
                message['like_count'] = like['like_count']
        if 'like_count' not in message:
            message['like_count'] = 0
        

    return render_template("landing.html", user_data=user_data, all_messages=all_messages, like_count=like_count) #sends user_data, all_messages, like_count to landing.html

#posts new message
@app.route("/add", methods = ['POST'])
def add():
    is_valid = True
    #checking to make sure the message passes validation
    if len(request.form['message']) < 5:
        is_valid = False
        flash("Message must be at least 5 characters")
    #if message passes validation, insert message into messages database
    if is_valid:
        mysql = connectToMySQL("enhanced_wall")
        query = "INSERT INTO messages (content, author, created_at, updated_at) VALUES (%(mess)s, %(auth)s, NOW(), NOW())"
        data = {
            'mess': request.form['message'],
            'auth': session['user_id']
        }
        mysql.query_db(query, data)
        flash("Message Added Successfully")
    return redirect("/landing")

#delete message
@app.route("/delete/<message_id>")
def delete(message_id):
    query = "DELETE FROM messages WHERE message_id = %(ms)s"
    data = {
        'ms': message_id
    }
    mysql = connectToMySQL('enhanced_wall')
    delete_message = mysql.query_db(query, data)
    return redirect("/landing")

#show details
@app.route("/details/<message_id>")
def details(message_id):
    #if user is not logged in, return to login page
    if 'user_id' not in session:
        return redirect("/")
    #if user is logged in, retrieve user information for specific user session
    mysql = connectToMySQL('enhanced_wall')
    query = "SELECT * FROM users WHERE user_id = %(id)s"
    data = {
        'id': session['user_id']
    }
    result = mysql.query_db(query, data)
    
    if result: #if a user exists with that user_id, select the first user in the user table (should only be one)
        user_data = result[0]

    #join user to their messages to display information
    mysql = connectToMySQL('enhanced_wall')
    query = "SELECT users.user_id, users.first_name, users.last_name, messages.message_id, messages.content, messages.author, messages.created_at FROM messages JOIN users ON messages.author = users.user_id WHERE message_id = %(ms)s"
    data = {
        'ms': message_id
    }
    detail_message = mysql.query_db(query, data)
    print(detail_message)

    mysql = connectToMySQL('enhanced_wall')
    query = "SELECT message_like, user_like FROM likes WHERE user_like= %(user_id)s"
    data = {
        'user_id': session['user_id']
    }
    liked_messages = [message['message_like'] for message in mysql.query_db(query,data)]
    
    #query to determine the users names that have liked the message
    mysql = connectToMySQL('enhanced_wall')
    query = "SELECT likes.message_like, likes.user_like, users.first_name, users.last_name FROM likes JOIN users ON likes.user_like = users.user_id WHERE message_like = %(ms)s"
    data = {
        'ms': message_id
    }
    like_list = mysql.query_db(query, data)
    
    return render_template("details.html", user_data=user_data, detail_message=detail_message[0], liked_messages=liked_messages, like_list=like_list)

#user likes message, add to likes table
@app.route("/details/like/<message_id>")
def like(message_id):
    mysql = connectToMySQL('enhanced_wall')
    query = "INSERT INTO likes (user_like, message_like) VALUE (%(user_id)s, %(message_id)s)"
    data = {
        'user_id': session['user_id'],
        'message_id': message_id
    }
    mysql.query_db(query, data)
    #returns to the details page and sends the message_id through
    return redirect(url_for('details', message_id=message_id))

#user unlikes message, delete from likes table
@app.route("/details/unlike/<message_id>")
def unlike(message_id):
    mysql = connectToMySQL('enhanced_wall')
    query = "DELETE FROM likes WHERE user_like = %(user_id)s AND message_like = %(message_id)s"
    data = {
        'user_id': session['user_id'],
        'message_id': message_id
    }
    mysql.query_db(query, data)
    #returns to the details page and sends the message_id through
    return redirect(url_for('details', message_id=message_id))

#logs out user
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)