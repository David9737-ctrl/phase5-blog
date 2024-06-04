from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from config import db

class User(db.Model):
    __tablename__='usertable'
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String)
    password=db.Column(db.String)
    posts=db.relationship('Blogpost', backref='user', lazy=True)
class Blogpost(db.Model):
    __tablename__='blogtable'
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String)
    userid=db.Column(db.Integer, db.ForeignKey("usertable.id"))
