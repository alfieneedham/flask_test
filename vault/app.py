from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY']='dgjsdfj6gfdj'
conn = sqlite3.connect('vault/users.db')

ACCESS_CODE = "42"
        
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

        return(render_template("welcome.html", realname = "REALNAME"))
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
        
        if str(accesscode) == ACCESS_CODE and password == password2:
            
            cur = conn.cursor()
            cur.execute('''SELECT USERNAME
                            FROM USERSDB
                            WHERE USERNAME=?''',
                            (username))
            result = cur.fetchone()

            if not result:
                conn.execute('''INSERT INTO USERSDB (USERNAME, REALNAME, PASSWORD)
                                VALUES (?,?,?)''', [username, realname, password])
                conn.commit()
                return(redirect(url_for("login")))
            else:
                return(render_template("register.html", form=form, loggedin=loggedin))      
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