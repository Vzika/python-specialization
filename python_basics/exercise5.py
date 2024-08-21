#calculate the bmi = weight/height**2
	
def bmi():
	weight = int(input("enter your weight in kg"))

	height = float(input("enter your height"))

	new_height = height ** 2
	bmi = int(weight) / int(new_height)
	if bmi < 16:
		print("your are severely under weight")
	elif bmi < 18:
		print("you are moderately under weight")
	elif bmi < 25:
		print("you are normal")

	else:
		print('you are obese')

bmi()
