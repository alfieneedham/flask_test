from flask import Flask, render_template, redirect, url_for



app = Flask(__name__)
app.config['SECRET_KEY']='fdsgidsf34g'

maze = {"A": "B",
        "B": "A,C,D,E",
        "C": "B",
        "D": "B"}



@app.route('/', methods=["GET","POST"])
def index():
    return redirect(url_for('traverse', currentVertex="A"))

@app.route('/traverse/<currentVertex>')
def traverse(currentVertex):
    currentNeighbours=maze[currentVertex].split(",")
    return render_template("vertex.html", vertex=currentVertex, neighbours=currentNeighbours)