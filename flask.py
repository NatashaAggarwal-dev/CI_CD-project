from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "<h1>Welcome to My Flask App</h1><p>Go to /hello/yourname to get a personal message.</p>"

@app.route('/hello/<name>')
def greet(name):
    return f"<h2>Hello, {name.capitalize()}! 👋</h2>"

@app.route('/square/<int:number>')
def square(number):
    result = number ** 2
    return f"<h2>The square of {number} is {result}.</h2>"

if _name_ == '_main_':
    app.run(host='0.0.0.0, port=5000)
