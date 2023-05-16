from flask import Flask, redirect, url_for, request

maze = {"A": ["B"],
        "B": ["A","C","D"],
        "C": ["B"],
        "D": ["B"]}

app = Flask(__name__)

@app.route('/')
def index():
    return '''<h1>Title</h1>
            <p>Info</p>'''

@app.route('/maze/<vertex>')
def A(vertex):
    upper = vertex.upper()
    routes = maze[str(upper)]
    return f'''<h1>You start from A. You have to reach D.</h1>
            <p>From ['{upper}'], you can go to {routes}'''
