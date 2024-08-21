from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")

def login():
  return render_template("login.html", user=None)

@auth.route("/logout")
def logout():
  return "Logout"

@auth.route("/sign_up")
def sign_up():
  return render_template("sign_up.html", user=None)


@auth.route("/signout")
def signout():
  return "signout"