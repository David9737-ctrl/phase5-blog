#!/usr/bin/env python3

from app import app
from models import db, User, Blogpost, loginform, registerform, registration
from faker import Faker
from werkzeug.security import generate_password_hash


faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")
        user1=User(username="davekickass", password="abc")
        user2=User(username="skippy12", password="123")
        post1=Blogpost(content='This is Davids\'s first post!', user=user1)
        post2=Blogpost(content='this is skippys first post!', user=user2 )
        post3=Blogpost(content="this is another random just to test!!", user=user1)
        post4= Blogpost(content="this is YET another test!!", user=user2)
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(post1)
        db.session.add(post2)
        db.session.add(post3)
        db.session.add(post4)
        db.session.commit()
                
        print("Seeding complete!")