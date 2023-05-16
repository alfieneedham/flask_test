from flask import Flask, render_template

app = Flask(__name__)
app.congif['SECRET_KEY']='fdsgidsf34g'

maze = {"A": ["B"],
        "B": ["A","C","D"],
        "C": ["B"],
        "D": ["B"]}

vertex = "A"
neighbours = maze[vertex]

@app.route('/', methods=["GET","POST"])
def traverse():
    render_template("vertex.html", vertex, neighbours)