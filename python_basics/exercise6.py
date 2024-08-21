#WAP to checkm if a year is a leap year or not

def leap_year():
	year = int(input("enter a year lets give an answer "))
	if year % 4 != 0:
		#print(f"{year} is not a leap year")
		if year %100 != 0:
		#	print(f"{year} is not a leap year")
			if (year % 400 != 0):
				print(f"{year} is not a leap year")
			else:
				print(f"{year} is a leap year")
		else:
			print(f"{year} is a leap year")
	else:
		print(f'{year} is  a leap yaer')

leap_year()
