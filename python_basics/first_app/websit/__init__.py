from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = "gghhahhhh"
  app.config['SQLALCHEMY_DATABASE_URL'] = "mysql+pymysql://Vzika:Zika1997#@localhost:3306/mysql"
  return app
