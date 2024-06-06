# some of these will be packages to help with the user authentication. 
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, redirect, url_for, flash, Flask
from sqlalchemy.orm import validates
from wtforms.validators import DataRequired, Length, EqualTo
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from wtforms import StringField, PasswordField, SubmitField
from config import db, app
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash


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
#  the registration class
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
# the login class
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)


    
