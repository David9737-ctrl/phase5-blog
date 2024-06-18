#!/usr/bin/env python3
import os
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, app
from flask_bcrypt import Bcrypt
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin
from models import User, Blogpost, registerform, loginform# import your models here!

# just setting up my flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = "Colombia12$"
db=SQLAlchemy(app)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False
db.init_app(app)
Bcrypt= Bcrypt(app)
# this will be the section for the class. sorry Chett I know this isnt the flatiron way lol
class User(db.Model, SerializerMixin, UserMixin):
    __tablename__='user'
    id=db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username=db.Column(db.String)
    password=db.Column(db.String, nullable=False)

# this is the admin register section
@app.route('/')
def register():
        return render_template ("homepage.html") 

@app.route('/loginpage', methods=['GET', 'POST'])
def signup():
    form = loginform()
    return render_template("login.html",form=form)

@app.route('/adminsignup', methods=['GET', 'POST'])
def userlogin():
    form = registerform()

    if form.validate_on_submit():
         hashed_password = Bcrypt.generate_password_hash(form.password.data)
         new_user= User(username=form.username.data, password=hashed_password)
         db.session.add(new_user)
         db.ession.commit()
         return redirect(url_for('/loginpage'))
    return render_template('register.html', form=form)

@app.route('/home')
def homepage():
    return render_template('mainhome.html')


@app.route('/blogposting')
def blog():
    return 'This is the page where you can post. Feel free to type away your thoughts, feelings, and opinions. Happy Blogging!!'

@app.route('/account')
def account():
    return 'hi this is my account how you doing'



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)