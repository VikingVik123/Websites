from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "Login page"

@auth.route("/sign up")
def sign_in():
    return "Sign up page"

@auth.route("/sign in")
def sign_up():
    return "Sign up page"