from models import Users
from add import session

all_users = session.query(Users).all()#this will create an instance of the User class, if form of list

#print(all_users[0].age)
for user in all_users:
  print(f"{user.id}, {user.name}, {user.age}")# this will print all the names in the table
  print

# single_users = session.query(Users).filter_by(id=2).all()
# print(single_users[0].name)
# print(single_users)
# single_users[0].name = "Emma"
# print(single_users[0].name)
# #session.commit()

#to delete

single_user = session.query(Users).filter_by(id=3).first()

session.delete(single_user)
session.commit()
ls
