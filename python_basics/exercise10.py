#WAP that accepts  peoples names and select the one to pay a bill randomly

def to_pay():
	import random

	names = input("enteryou names seperated by coma ")
	name_list = names.split(",")

	who_to_pay = random.choice(name_list)
	print(who_to_pay)

to_pay();
