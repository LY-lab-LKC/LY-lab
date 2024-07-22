import requests
from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/group")
def group():
    return render_template("group.html")

@app.route("/publication")
def publication():
    return render_template("publication.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
        return render_template("contact.html")


if __name__ == "__main__":
    app.run( debug=True)