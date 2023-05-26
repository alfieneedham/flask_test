from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from functions.dijkstras_algorithm import dijkstras_algorithm

adjList = {"Aylesbury": [["Brighton", 50], ["Cambridge", 10], ["Dunstable", 100], ["Falmouth", 75]],
        "Brighton": [["Aylesbury", 50], ["Cambridge", 25]],
        "Cambridge": [["Aylesbury", 10], ["Brighton", 25], ["Eynsham", 40]],
        "Dunstable": [["Aylesbury", 100], ["Falmouth", 60], ["Huntingdon", 50], ["Ipswich", 75]],
        "Eynsham": [["Cambridge", 40], ["Ipswich", 5]],
        "Falmouth": [["Aylesbury", 75], ["Dunstable", 60]],
        "Grasmere": [["Huntingdon", 30]],
        "Huntingdon": [["Dunstable", 50], ["Grasmere", 30], ["Ipswich", 100], ["Kensington", 200]],
        "Ipswich": [["Dunstable", 75], ["Eynsham", 5], ["Jarrow", 10], ["Huntingdon", 100]],
        "Jarrow": [["Ipswich", 10], ["Kensington", 15]],
        "Kensington": [["Huntingdon", 200], ["Jarrow", 15], ["Longborough", 20]],
        "Longborough": [["Kensington", 20]]}

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
    towns = []
    route = ""
    for town in adjList:
        towns.append(town)

    form = RouteForm()
    
    if form.is_submitted():
        startnode=form.startnode.data
        endnode=form.endnode.data

        path = dijkstras_algorithm(adjList, startnode, endnode)
        for town in path[0]:
            route += town
            if town != path[0][-1]:
                route += ", "

        return render_template("calculate_route.html", towns=towns, route=route, distance=path[1])
    else:
        return render_template("calculate_route.html", towns=towns)

@app.route('/modify_weight', methods=['GET','POST'])
def modify_weight():
    return render_template("modify_weight.html")

if __name__=="__main__":
    app.run()