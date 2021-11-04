from enum import unique
from mongoengine.fields import EmailField, StringField
from .db import db  

class User(db.Document):
    print(db.Document._get_collection_name())
    username =StringField(required=True, unique=True)
    email = EmailField(required=True,unique=True)
    password =StringField(reqired=True)

