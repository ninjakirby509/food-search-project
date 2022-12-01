import os
import flask
import requests
from flask import session
from dotenv import load_dotenv,find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = flask.Flask(__name__)
app.secret_key= "My key"
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
#app.config['SECRET_KEY'] = 'SUPERSECRETKEY'
#yelp_db = SQLAlchemy(app)

@app.route('/')
def login():
    """The login in screen """
    return flask.render_template('signup.html')
@app.route('/signup_handler',methods = ['POST'])
def signup_handler():
    """Handle Login"""
    form_data = flask.request.form
    username = form_data["Username"]
    password = form_data["password"]
    return flask.render_template('login.html')
@app.route('/login_handler',methods = ['POST'])
def login_handler():
    """Handle Login"""
    print("Handle func")
    form_data = flask.request.form
    username = form_data["Username"]
    password = form_data["password"]
    return flask.render_template('index.html')


app.run(debug=True)