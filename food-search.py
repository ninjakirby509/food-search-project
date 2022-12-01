import os
import flask
import requests
from flask import session
from dotenv import load_dotenv,find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

load_dotenv(find_dotenv())
app = flask.Flask(__name__)
yelp_url = "https://api.yelp.com/v3"
search_url = "/businesses/search"
yelp_key = os.getenv("YELP_KEY")
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("LOCAL_DATABASE_URL")
app.config['SECRET_KEY'] = 'SUPERSECRETKEY'
yelp_db = SQLAlchemy(app)

class Person(yelp_db.Model):
    __tablename__ = 'Username'
    username = yelp_db.Column(yelp_db.String(50),primary_key = True)
    password = yelp_db.Column(yelp_db.String(50),unique = True)
    def __init__(self,username,password):
        self.username = username
        self.password = password
with app.app_context():
    yelp_db.create_all()
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
    thisuser = Person.query.filter_by(username=username).first()
    if thisuser is None:
        print("User does not exist")
        thisuser = Person(username,password)
        yelp_db.session.add(thisuser)
        yelp_db.session.commit()
    else:
        print("User Exit")
    return flask.render_template('login.html')


@app.route('/login_handler', methods = ['POST'])
def login_handler():
    """Handle Login"""
    print("Handle func")
    form_data = flask.request.form
    username = form_data["Username"]
    password = form_data["password"]
    thisuser = Person.query.filter_by(username=username).first()
    if thisuser is None:
        return flask.redirect(flask.url_for("login_handler"))
    else:
        return flask.redirect(flask.url_for("homepage"))
@app.route('/index')
def homepage():
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {yelp_key}"
    }
    location_data = flask.request.form
    params = {
        "location": location_data["location"] if location_data else "Hallettsville",
        "term": "food",
        "price": [1, 2, 3, 4],
        "sort_by": "distance"
    }
    response = requests.get(yelp_url+search_url, headers=headers, params=params)
    for business in response.json()["businesses"]:
        print("name:", business['name'])
        print("id:", business['id'])
        print("url:", business['url'])
    return flask.render_template('index.html', businesses = response.json()["businesses"])



app.run(debug=True)