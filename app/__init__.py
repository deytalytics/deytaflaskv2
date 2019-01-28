import sys

# Import flask and template operators
from flask import Flask

#import beautifulsoup
from bs4 import BeautifulSoup

#import urllib parser to parse parameters
from urllib.parse import parse_qs

#Import ability to mask passwords
from passlib.hash import sha256_crypt

import gc

# Import bootstrap
from flask_bootstrap import Bootstrap

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


import os, requests, json

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

#Define the database connection variables - should not be hardcoding these here
aws_db_hostname = 'ec2-50-16-196-138.compute-1.amazonaws.com'
aws_db_username = 'kbmymanebzaprn'
aws_db_password = 'a090dbaf8e346e65ea63436b9d22c6e709f786308c0f4744e4d257389c71a8fa'
aws_db_database = 'de3gnfncn93kt4'

gcp_db_username = 'postgres'
gcp_db_password = 'xedos123'
gcp_db_database = 'postgres'
gcp_db_instance_name = 'my-project-1497304749768:europe-west2:deytalytics1'

username=aws_db_username
password=aws_db_password
database = aws_db_database
hostname=aws_db_hostname
#instance_name=gcp_db_instance_name

#Setup database config variables for the app
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{pwd}@{url}/{db}'.format(user=username, pwd=password, url=hostname, db=database)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{pwd}@/{db}?host=/cloudsql/{instance_name}'.format(user=username, pwd=password, db=database, instance_name = instance_name)

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
