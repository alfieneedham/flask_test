from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

adjList = {"Aylesbury": [["Brighton", 0], ["Cambridge", 0], ["Dunstable", 0], ["Falmouth", 0]],
        "Brighton": [["Ayelsbury", 0], ["Cambridge", 0]],
        "Cambridge": [["Ayelsbury", 0], ["Brighton", 0], ["Eynsham", 0]],
        "Dunstable": [["Ayelsbury", 0], ["Falmouth", 0], ["Huntingdon", 0], ["Ipswich", 0]],
        "Eynsham": [["Cambridge", 0], ["Ipswich", 0]],
        "Falmouth": [["Ayelsbury", 0], ["Dunstable"]],
        "Grasmere": [["Huntingdon", 0]],
        "Huntingdon": [["Dunstable", 0], ["Grasmere", 0], ["Ipswich", 0], ["Kensington", 0]],
        "Ipswich": [["Dunstable", 0], ["Eynsham", 0], ["Jarrow", 0], ["Huntingdon", 0]],
        "Jarrow": [["Ipswich", 0], ["Kensington", 0]],
        "Kensington": [["Huntingdon", 0], ["Jarrow", 0], ["Longborough", 0]],
        "Longborough": [["Kensington", 0]]}

app = Flask(__name__)
app.config['SECRET_KEY']='s9j4jfj8cnr98g'

# class RouteForm(FlaskForm):
#     town1 = 

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("calculate_route.html")

if __name__=="__main__":
    app.run()