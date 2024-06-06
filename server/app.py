#!/usr/bin/env python3
# most of these down below will mostly be packages for authentication
from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from wtforms.validators import DataRequired, Length, EqualTo
from sqlalchemy.ext.associationproxy import association_proxy
# from sqlalchemy_serializer import SerializerMixin
from wtforms import StringField, PasswordField, SubmitField
from config import db, app
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Blogpost# import your models here!



# down here below are the routes of my web app
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the homepage!'

@app.route('/blogposting')
def blog():
    return 'This is the page where you can post. Feel free to type away your thoughts, feelings, and opinions. Happy Blogging!!'

@app.route('/account')
def account():
    return 'hi this is my account how you doing'

# this is the login route
@app.route('/login',methods=['GET', 'POST'])
def login():
    form = login()
    if form.validate_on_submit():
        user= User.query.where(User.username==request.json['username']).first()
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            flash('Logged in successfully!', 'success'), 201
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'incorrect'), 401
    return render_template('login.html', form=form)


@app.get('/')
def index():
    return "Hello world"


if __name__ == '__main__':
    app.run(port=5555, debug=True)