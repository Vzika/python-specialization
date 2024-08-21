#LOVE CALCULATOR
#WAP TO CHECH  the % percentageof love btwn u and ur partner
#use the TRUE LOVE method
#by count the amount of time the letters, T,R,U,E,L,O,V,E, appers in your name and that of ur partner

#e.g if TRUE appers 2 times, and LOVE appears 5 times in the both name
# concatenate the two numbers to give u 25%

def love_calculator():
	your_name = input("enter you name? ")
	partners_name = input("enter your partners name ")
	true = "true"	
	luv = "love"
	tcount1 = 0;
	tcount2 = 0;
	lcount1 = 0;
	lcount2 = 0;
	for i in true:
		if i in your_name.lower():
			counting1 =(your_name.count(i))
			tcount1 = tcount1 + counting1
		
		if i in partners_name.lower():
			counting2 =(partners_name.count(i))
			tcount2 = tcount2 + counting2
		total_count1 = tcount1 +tcount2 
	print(total_count1)
	
	for j in luv:
		if j in your_name.lower():
			lcounting1 =(your_name.count(j))
			lcount1 = lcount1 + lcounting1
		
		if j in partners_name.lower():
			lcounting2 =(partners_name.count(j))
			lcount2 = lcount2 + lcounting2
		total_lcount2 = lcount1 +lcount2 
	print(total_lcount2)
	
	str_total_true_count = str(total_count1)
	str_total_love_count = str(total_lcount2)

	love_perc = str_total_true_count + str_total_love_count
	print(f"your love % is {love_perc}%")
	love_match = int(love_perc)
	if love_match <=40:
		print(f"your love % is {love_perc}%, and your love is not sure yet")
	elif love_match <=50:
		print(f"your love % is {love_perc}%,and you are good together")
	else:
		print(f"your love % is {love_perc}. goodluck!")







love_calculator();	
