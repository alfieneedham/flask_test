from flask import Flask, render_template
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY']='qlfb8fhsnv9rhb8'

login_history = []

class LoginForm(FlaskForm):
    username = StringField("Username")
    submit = SubmitField("Log In")

@app.route('/', methods=["GET","POST"])
def login():
    entry_form = LoginForm()

    if entry_form.is_submitted():
        username = entry_form.username.data
        if username == "":
            return render_template("login.html", form=entry_form)
        elif username != "admin":
            login_history.append((username,datetime.now().strftime("%H:%M:%S")))
            return render_template("user.html", username=username, count=len(login_history)-1)
        else:
            return render_template("admin.html", history=login_history)

    return render_template("login.html", form=entry_form)