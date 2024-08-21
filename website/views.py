from flask import Blueprint

views = Blueprint("vies", __name__)

@views.route("/")
def home():
  return "this is the home page"