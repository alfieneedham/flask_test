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
        
class LoginForm(FlaskForm):
    username = StringField("username")
    password = StringField("password")
    submit = StringField("submit")
    
class RegisterForm(FlaskForm):
    realname = StringField("realname")
    username = StringField("username")
    password = StringField("password")
    password2 = StringField("password2")
    accesscode = StringField("accesscode")
    submit = StringField("submit")

@app.route('/')
def index():
    username = session.get('username', None)
    if username is not None:
        print(username)
        print (users[username].realname)
        return(render_template("welcome.html", realname = users[username].realname))
    else:
        return(redirect(url_for("login")))

@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get('username', None) is None:
        loggedin = False
    else:
        loggedin = True
    form=RegisterForm()
    if form.is_submitted():
        realname=form.realname.data
        username=form.username.data
        password=form.password.data
        password2=form.password2.data
        accesscode=form.accesscode.data
        
        if str(accesscode) == ACCESS_CODE and password == password2 and username not in users:
            new_user = User(realname, username, password)
            users[username] = new_user
            return(redirect(url_for("login")))
        else:
            return(render_template("register.html", form=form, loggedin=loggedin))
    else:
        return(render_template("register.html", form=form, loggedin=loggedin))
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get('username', None) is None:
        loggedin = False
    else:
        loggedin = True
    form = LoginForm()
    if form.is_submitted():
        username=form.username.data
        password=form.password.data
        user_info = users.get(username, None)
        if user_info is not None and user_info.password == password:
            session["username"] = username
            return(redirect(url_for("index")))
        else:
            return render_template("login.html", form=form, loggedin=loggedin)
    else:
        return(render_template("login.html", form=form, loggedin=loggedin))
    
@app.route("/logout")
def logout():
    del session["username"]
    return(redirect(url_for("login")))