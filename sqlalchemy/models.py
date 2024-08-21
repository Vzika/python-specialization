from sqlalchemy import create_engine, Column,Integer,String
from sqlalchemy.orm import declarative_base
import os

#dialect+driver://username:password@host:port/database

username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
name = os.getenv("DB_NAME")

# print(username)
# print(password)
# print(host)
# print(port)
# print(name)

url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{name}"
print(url)
engine = create_engine(url)

Base = declarative_base()

class Users(Base):
  __tablename__ = "users"
  id = Column(Integer,primary_key ="true")
  name = Column(String(255))
  age = Column(Integer)

Base.metadata.create_all(engine)