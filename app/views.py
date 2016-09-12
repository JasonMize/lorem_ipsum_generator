from flask import render_template

from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {
        "full_name": "Jason Mize",
        "username": "jasonmize",
    }


    return render_template("index.html", user=user)