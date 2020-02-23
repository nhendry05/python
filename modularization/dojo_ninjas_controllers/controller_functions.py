from flask import render_template, redirect, request
from config import db
from models import Dojo, Ninja

def index():
    all_dojos = Dojo.query.all()
    all_ninjas = Ninja.query.all()
    return render_template("index.html", all_dojos=all_dojos, all_ninjas=all_ninjas)

def add_dojo():
    new_dojo = Dojo(name=request.form['dojo_name'], city=request.form['city'], state=request.form['state'])
    db.session.add(new_dojo)
    db.session.commit()
    return redirect("/")

def add_ninja():
    new_ninja = Ninja(first_name=request.form['fname'], last_name=request.form['lname'], dojo_id=request.form['dojo_id'])
    db.session.add(new_ninja)
    db.session.commit()
    return redirect("/")
