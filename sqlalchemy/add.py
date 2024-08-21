from sqlalchemy.orm import sessionmaker
from models import Users, engine

Session = sessionmaker(bind=engine)
session = Session()

user1 = Users(name="Zika", age=30)
user2 = Users(name="vee", age=24)
user3 = Users(name="Michelle", age=2)
user4 = Users(name="Charles", age=35)
user5 = Users(name="Afo", age=20)

#session.add(user1)
#session.add(user2)
#session.add(user3)
#session.add(user4)
#session.add(user5)

session.commit()

