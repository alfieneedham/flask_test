from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY']='dgjsdfj6gfdj'

ACCESS_CODE = "42"

users={}

class User():
    def __init__(self, realname, username, password):
        self.realname = realname
        self.username = username
        self.password = password

@app.route('/')
def index():
    return redirect(url_for('welcome'))