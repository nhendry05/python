from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL("create_read")
    pets = mysql.query_db("SELECT * FROM pets;")
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route("/add_pet", methods = ["POST"])
def add_pet_to_db():
    mysql = connectToMySQL("create_read")
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(pn)s, %(pt)s, NOW(), NOW());"
    data = {
        "pn": request.form["pname"],
        "pt": request.form["ptype"]
    }
    new_pet_id = mysql.query_db(query, data)
    #query = f"INSERT INTO pets (name, type, created_at, updated_at) VALUES ('{request.form['pname']}', '{request.form['ptype']}', NOW(), NOW());"
    #new_pet_id = mysql.query_db(query)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)