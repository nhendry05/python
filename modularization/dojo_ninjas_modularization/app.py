from flask import Flask, render_template, redirect, request, url_for
from sqlalchemy.sql import func
from config import app, db

class Dojo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Ninja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    dojo_id = db.Column(db.String(45), db.ForeignKey("dojo.id", ondelete="cascade"), nullable=False)
    dojo = db.relationship('Dojo', foreign_keys=[dojo_id], backref="dojo_ninja")
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())



@app.route("/", methods = ['GET','POST'])
def index():
    all_dojos = Dojo.query.all()
    all_ninjas = Ninja.query.all()
    return render_template("index.html", all_dojos=all_dojos, all_ninjas=all_ninjas)

@app.route("/add_dojo", methods=["POST"])
def add_dojo():
    new_dojo = Dojo(name=request.form['dojo_name'], city=request.form['city'], state=request.form['state'])
    db.session.add(new_dojo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/add_ninja", methods=["POST"])
def add_ninja():
    new_ninja = Ninja(first_name=request.form['fname'], last_name=request.form['lname'], dojo_id=request.form['dojo_id'])
    db.session.add(new_ninja)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)