#WAP to find out how many days weeks and months once have left to live until 90 years ols
#take input from the user
#your output should be in this order
#you have a day, b weeks and c months left
#1 year is 365 days
#1 year is 52 weeks
#1 year is 12 months

def how_longto_live():
	current_age = int(input("enter your current age "))
	if current_age <= 90:
		year_left = 90 - current_age
		month_left = 12 * year_left
		week_left = 52 * year_left
		day_left = 365 * year_left
	print(f"you have {day_left} days left, {week_left} weeks left and {month_left} months left")


how_longto_live();
