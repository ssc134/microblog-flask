from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = dict({"username": "Saurabh"})
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
        {"author": {"username": "Jellybean"}, "body": "Meowwww"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
