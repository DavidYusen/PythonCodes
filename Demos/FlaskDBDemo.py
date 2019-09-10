import datetime
from flask import Flask
from peewee import *
from playhouse.flask_utils import FlaskDB

DATABASE = 'postgresql://postgres:password@localhost:5432/my_database'

app = Flask(__name__)
app.config.from_object(__name__)

db_wrapper = FlaskDB(app)


class User(db_wrapper.Model):
    username = CharField(unique=True)


class Tweet(db_wrapper.Model):
    user = ForeignKeyField(User, backref='tweets')
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
