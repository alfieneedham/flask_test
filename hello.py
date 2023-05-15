from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''<h1>Index Page</h1>
            <p>ComputerScienceGang let's go<p>'''

@app.route('/goodbye')
def goodbyePage():
    return '''<h1>Goodbye Page</h1>
            <p>bye bye :(</p>'''

@app.route('/greet/<name>')
def greet(name):
    title = name.title()
    return f'''<h1>Hello, {title}.</h1>
            <p>I've been expecting you.</p>'''

@app.route('/admin')
def hello_admin():
    return '<h1>Hello Admin</h1>'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f'<h1>Hello {guest} as Guest</h1>'

@app.route('/user/<name>')
def hello_user(name):
    title = name.title()
    if title == 'Admin':
        return redirect(url_for('hello_admin'))
    else: 
        return redirect(url_for('hello_guest', guest = title))
    
@app.route('/analyze')
def analyzeRequest():
    print('Headers: ', request.headers)
    print('Args: ', request.args)
    return '''<h1>Check Flask console for details.</h1>'''

@app.route('/birthdate/<DoB>')
def displayDoB(DoB):
    return f'''<h1>Date of Birth:</h1>
            <p>{DoB}'''

@app.route('/pass/<password>')
def passwordCheck(password):
    if password == "abCdE123":
        return '<h1>Correct!</h1>'
    else:
        return '<h1>Wrong :(</h1>'
    
@app.route('/prime/<number>')
def isPrime(number):
    num = int(number)

    def checkIfPrime(num):
        if num == 1:
            prime = False
        else:
            prime = True
            for n in range(round(num/2)):
                if (n+1)!=1 and (n+1)!= num:
                    if num%(n+1) == 0:
                        prime = False
        return(prime)

    def findNextPrime(num):
        check = num
        foundNext = False
        while foundNext == False:
            check += 1
            if checkIfPrime(check) == True:
                foundNext = True
        return(check)
    
    if checkIfPrime(num) == True:
        return f'<h1>{num} is prime.</h1>'
    else:
        return f'<h1>{num} is not prime. The next prime is {findNextPrime(num)}.</h1>'