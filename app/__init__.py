import sys

# Import flask and template operators
from flask import Flask

#import beautifulsoup
from bs4 import BeautifulSoup

#import urllib parser to parse parameters
from urllib.parse import parse_qs

#Import ability to mask passwords
#from passlib.hash import sha256_crypt

#import gc

# Import bootstrap
from flask_bootstrap import Bootstrap

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


import os, requests, json

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

#Setup database config variables for the app
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['username']=os.environ['USERNAME']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
app.config['SQLALCHEMY_POOL_RECYCLE']=int(os.environ['SQLALCHEMY_POOL_RECYCLE'])

#Set up the database using the config variables
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)

from app import models
from app import views
from app import forms			

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
