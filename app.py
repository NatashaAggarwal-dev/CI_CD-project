from flask import Flask
app=Flask(__name__)
@app.route("/info")
def myinfo():
    return "My name is Mohammad Rehan, Proud to be a student of LinuxWorld, learning under the mentorship of the legendary Vimal Daga Sir."
@app.route("/phone")
def myphone():
    return "9594203168"
app.run(host="0.0.0.0")
