# some of these will be packages to help with the user authentication. 
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from config import db, app

# app = Flask(__name__)
# this is the user class
class User(db.Model, SerializerMixin):
    __tablename__='usertable'
    id=db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username=db.Column(db.String)
    password=db.Column(db.String)
    posts=db.relationship('Blogpost', backref='user', lazy=True)
    serialize_rules=['-posts.user']
# this will be the posting class
class Blogpost(db.Model, SerializerMixin):
    __tablename__='blogtable'
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    content=db.Column(db.String)
    userid=db.Column(db.Integer, db.ForeignKey("usertable.id"))
    serialize_rules=['-user.posts']


    
