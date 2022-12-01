import os
import flask
import requests
from flask import session
from dotenv import load_dotenv,find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = flask.Flask(__name__)
yelp_url = "https://api.yelp.com/v3"
search_url = "/businesses/search"
yelp_key = os.getenv("YELP_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SECRET_KEY'] = 'SUPERSECRETKEY'
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


@app.route('/login_handler', methods = ['POST'])
def login_handler():
    """Handle Login"""
    print("Handle func")
    form_data = flask.request.form
    username = form_data["Username"]
    password = form_data["password"]
    return flask.render_template('index.html')


@app.route('/index')
def homepage():
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {yelp_key}"
    }
    params = {
        "location": "Hallettsville",
        "term": "food",
        "price": [1,2,3,4],
        "sort_by": "distance"
    }
    response = requests.get(yelp_url+search_url, headers=headers, params=params)
    for business in response.json()["businesses"]:
        print("name:", business['name'])
        print("id:", business['id'])
        print("url:", business['url'])
    return flask.render_template('index.html', businesses = response.json()["businesses"])


app.run(debug=True)