from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY']='dgjsdfj6gfdj'
conn = sqlite3.connect('vault/users.db', check_same_thread=False)

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
        
        cur = conn.cursor()
        cur.execute("SELECT REALNAME FROM USERSDB WHERE USERNAME=?",[username])
        result = cur.fetchone()[0] 

        return(render_template("welcome.html", realname=result))
    else:
        return(redirect(url_for("login")))

@app.route("/register", methods=["GET", "POST"])
def register():

    if session.get('username', None) is None:
        loggedin = False
    else:
        loggedin = True

    form=RegisterForm()
    
    errorpassword = "The passwords do not match."
    erroraccesscode = "The access code is incorrect."
    errorusername = "This username has already been taken."
    
    if form.is_submitted():
        realname=form.realname.data
        username=form.username.data
        password=form.password.data
        password2=form.password2.data
        accesscode=form.accesscode.data
        
        if str(accesscode) == ACCESS_CODE:
            if password == password2: 
                
                cur = conn.cursor()
                cur.execute('''SELECT USERNAME
                            FROM USERSDB
                            WHERE USERNAME=?''',
                            [username])
                result = cur.fetchone()

                if not result:
                    conn.execute('''INSERT INTO USERSDB (USERNAME, REALNAME, PASSWORD)
                                    VALUES (?,?,?)''', [username, realname, password])
                    conn.commit()
                    
                    print("Successful registration. Name input:", realname, ";", "Username input:", username, ";", "Password input:", password)
                    return redirect(url_for("login"))
                
                else:
                    print("Registration failed. Username already taken. Username input:", username)
                    return render_template("register.html", form=form, loggedin=loggedin, error=errorusername)
            
            else:
                print("Registration failed. Password mismatch. Password input:", password, ";", "Password2 input:", password2)
                return render_template("register.html", form=form, loggedin=loggedin, error=errorpassword)     
        else:
            print("Registration failed. Incorrect access code. Name input:", realname, ";", "Access code input:", accesscode, ";", "Expected access code:", ACCESS_CODE)
            return render_template("register.html", form=form, loggedin=loggedin, error=erroraccesscode)
    else:
        return render_template("register.html", form=form, loggedin=loggedin)
    
@app.route("/login", methods=["GET", "POST"])
def login():
    
    errormessage = "Username or password incorrect."
    
    if session.get('username', None) is None:
        loggedin = False
    else:
        loggedin = True

    form = LoginForm()
    if form.is_submitted():
        username=form.username.data
        password=form.password.data

        cur = conn.cursor()
        cur.execute("SELECT PASSWORD FROM USERSDB WHERE USERNAME=?",[username])
        result = cur.fetchone()

        if result is not None:
            if password == result[0]:
                print("Login successful. User:", username)
                session["username"] = username
                return(redirect(url_for("index")))
            
            else:
                print("Login unsuccessful. Incorrect password. Username input:", username, ";", "Password input:", password, ";", "Expected password:", result[0])
                return render_template("login.html", form=form, loggedin=loggedin, error=errormessage)

        else:
            print("Login unsuccessful. Invalid username. Username input:", username, ";", "Password input:", password)
            return render_template("login.html", form=form, loggedin=loggedin, error=errormessage)
        
    else:
        return render_template("login.html", form=form, loggedin=loggedin)
    
@app.route("/logout")
def logout():
    print("User logged out. User:", session["username"])
    del session["username"]
    return(redirect(url_for("login")))

if __name__ == "__main__":
    app.run()