from flask import Blueprint
from flask import render_template

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template("index.html") 

@views.route("/about")
def about():
    return "<h2>About PAGE<h2>"