#!/usr/bin/env python3
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, app
from models import User, Blogpost# import your models here!



# down here below are the routes of my web app
app = Flask(__name__)

# this is the admin register section
@app.route('/')
def register():
        return render_template ("register.html")

@app.route('/adminsignup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route('/loginpage')
def userlogin():
    return render_template('login.html')

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
    app.run(port=5555, debug=True)