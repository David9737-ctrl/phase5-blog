# some of these will be packages to help with the user authentication. 
import os
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from config import db, app
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

# app = Flask(__name__)
# CORS(app)

# Bcrypt= Bcrypt(app)
# this is the user class
class User(db.Model, SerializerMixin, UserMixin):
    __tablename__='user'
    id=db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username=db.Column(db.String)
    password=db.Column(db.String, nullable=False)
    # posts=db.relationship('Blogpost', backref='user', lazy=True)
    # serialize_rules=['-posts.user']
# this will be the posting class
class Blogpost(db.Model, SerializerMixin):
    __tablename__='blogtable'
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    content=db.Column(db.String)
    userid=db.Column(db.Integer, db.ForeignKey("usertable.id"))
    serialize_rules=['-user.posts']

class registerform(FlaskForm):
    username= StringField(validators=[InputRequired(), Length( min =4, max=20)], render_kw={"placeholder": "Username"})
    password=PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                "Username already taken. Please choose a different Username ")
class loginform(FlaskForm):
    username= StringField(validators=[InputRequired(), Length( min =4, max=20)], render_kw={"placeholder": "Username"})
    password=PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

    
