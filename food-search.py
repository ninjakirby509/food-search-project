import os
import flask
import requests
from flask import session
from dotenv import load_dotenv,find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = flask.Flask(__name__)
app.secret_key= "My key"

@app.route('/')
def login():
    """The login in screen """
    return flask.render_template('login.html')


app.run(debug=True)