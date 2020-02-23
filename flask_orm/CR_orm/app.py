from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cr_orm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    age = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

@app.route("/", methods = ['GET','POST'])
def index():
    all_users = User.query.all()
    return render_template("index.html", all_users=all_users)

@app.route("/add", methods=["POST"])
def add():
    new_user = User(first_name=request.form['fname'], last_name=request.form['lname'], email=request.form['email'], age=request.form['age'])
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)