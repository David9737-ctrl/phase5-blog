#!/usr/bin/env python3
from flask import Flask, request, session
from config import app, db
from models import User, Blogpost # import your models here!

@app.route('/')
def home():
    return 'Welcome to the homepage!'

@app.route('/blogposting')
def blog():
    return 'This is the page where you can post. Feel free to type away your thoughts, feelings, and opinions. Happy Blogging!!'


@app.get('/')
def index():
    return "Hello world"


if __name__ == '__main__':
    app.run(port=5555, debug=True)