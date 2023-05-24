from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from functions.dijkstras_algorithm import dijkstras_algorithm

adjList = {"Aylesbury": [["Brighton", 1], ["Cambridge", 1], ["Dunstable", 1], ["Falmouth", 1]],
        "Brighton": [["Aylesbury", 1], ["Cambridge", 1]],
        "Cambridge": [["Aylesbury", 1], ["Brighton", 1], ["Eynsham", 1]],
        "Dunstable": [["Aylesbury", 1], ["Falmouth", 1], ["Huntingdon", 1], ["Ipswich", 1]],
        "Eynsham": [["Cambridge", 1], ["Ipswich", 1]],
        "Falmouth": [["Aylesbury", 1], ["Dunstable"]],
        "Grasmere": [["Huntingdon", 1]],
        "Huntingdon": [["Dunstable", 1], ["Grasmere", 1], ["Ipswich", 1], ["Kensington", 1]],
        "Ipswich": [["Dunstable", 1], ["Eynsham", 1], ["Jarrow", 1], ["Huntingdon", 1]],
        "Jarrow": [["Ipswich", 1], ["Kensington", 1]],
        "Kensington": [["Huntingdon", 1], ["Jarrow", 1], ["Longborough", 1]],
        "Longborough": [["Kensington", 1]]}

app = Flask(__name__)
app.config['SECRET_KEY']='s9j4jfj8cnr98g'

class RouteForm(FlaskForm):
    startnode = SelectField("startnode")
    endnode = SelectField("endnode")
    submit = SubmitField("submit")


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('calculate_route'))

@app.route('/calculate_route', methods=['GET','POST'])
def calculate_route():
    form = RouteForm()
    
    if form.is_submitted():
        startnode=form.startnode.data
        endnode=form.endnode.data
        print(startnode, endnode)
        return render_template("calculate_route.html")
    else:
        return render_template("calculate_route.html")

@app.route('/modify_weight', methods=['GET','POST'])
def modify_weight():
    return render_template("modify_weight.html")

if __name__=="__main__":
    result = dijkstras_algorithm(adjList, "Aylesbury", "Ipswich")
    print("")
    print("Path: ", result)
    #app.run()