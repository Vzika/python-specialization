from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route("/")
def greet():
  return("hello world!")

@app.route("/hello/<name>")
def hello(name):
  return(f"hello {escape(name)}")

if __name__ == "main":
  app.run(debug=True)

# url_for()
#To build a URL to a specific function, use the url_for() function. It accepts the name of the function as 
# its first argument and any number of keyword arguments, each 
# corresponding to a variable part of the URL rule. Unknown variable 
# parts are appended to the URL as query parameters.

@app.route("/index")

def index():
  return("this is the index")

@app.route("/login/<username>")
def login(username):
  return(f"{username} login successful")

@app.route('/user/<username>')
def profile(username):
  return f'{username}\'s profile'

with app.test_request_context():
  print(url_for("index"))
  print(url_for("index", next = "/"))
  print(url_for("login", username ="zikavera" ))
  print(url_for('profile', username='John Doe'))
  
#outpt:
#/index
#/index?next=/
#/login/zika
#/user/John%20Doe

#HTMl request
#fron flask import request
@app.route('/to_login', methods=['GET', 'POST'])
def to_login():
  if request.method == 'POST':
    return do_the_login()
  else:
    return show_the_login_form()
  
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
  
#rendering template
#To render a template you can use the 
# render_template() method. All you have to do is provide the name of the template and 
# the variables you want to pass to the template engine as keyword arguments. 

from flask import render_template

@app.route('/say_hello/')
@app.route('/say_hello/<name>')
def say_hello(name=None):
  return render_template('hello.html', person=name)