#WAP to check if a number is even or odd 

def even_or_odd():
	number = int(input("enter a number "))
	if number % 2 == 0:
		print(f"{number} is even")
	else:
		print(f"{number} is odd")

even_or_odd();
