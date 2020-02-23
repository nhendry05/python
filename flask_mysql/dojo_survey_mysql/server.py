from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "jamesy"

@app.route('/')
def survey():
    query = "SELECT * FROM dojo"
    mysql = connectToMySQL('survey')
    all_users = mysql.query_db(query)
    print(all_users)
    return render_template("index.html", all_users = all_users)

@app.route('/create', methods = ['POST'])
def create_user():
    is_valid = True
    if len(request.form['name']) < 1:
        is_valid = False
        flash("***Please Enter a Name")
        return redirect ('/')
    if len(request.form['location']) < 1:
        is_valid = False
        flash("***Please Enter a Location")
        return redirect ('/')
    if len(request.form['language']) < 1:
        is_valid = False
        flash("***Please Enter a Language")
        return redirect ('/')
    if len(request.form['comment']) > 121:
        is_valid = False
        flash("***Comment must be less than 120 characters")
        return redirect ('/')
    if is_valid:
        mysql = connectToMySQL('survey')
        query = "INSERT INTO dojo (name, location, language, comment, created_at, updated_at) VALUES (%(nm)s, %(lo)s, %(lg)s, %(co)s, NOW(), NOW() )"
        data = {
            'nm': request.form['name'],
            'lo': request.form['location'],
            'lg': request.form['language'],
            'co': request.form['comment']
        }
        user_id = mysql.query_db(query, data)
        return redirect('/results/{}'.format(user_id))

@app.route('/results/<user_id>')
def results(user_id):
    mysql = connectToMySQL('survey')
    query = "SELECT * FROM dojo WHERE id = %(id)s"
    data = {
        'id': user_id
    }
    user = mysql.query_db(query, data)
    print(user)
    return render_template("results.html", user=user[0])

if __name__ == "__main__":
    app.run(debug=True)