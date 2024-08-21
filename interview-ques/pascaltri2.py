#Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

#Returns an empty list if n <= 0
#You can assume n will be always an integer

#[
# [1],          # Row 0
# [1, 1],       # Row 1
# [1, 2, 1],    # Row 2
# [1, 3, 3, 1], # Row 3
# [1, 4, 6, 4, 1] # Row 4
#]
 #formular for pascal triangle
# nCr = n! // r! (n - r)!  this will print the exact val in each row of pascal triangle


#where 
# n  =  row number
# r = column number

from math import factorial

def pascal_triangle():
	triangle =[] 
	rows = int(input("enter the number of rows "));
	if rows <= 0:
		return triangle;
	for n in range(rows):
		for r in range(n + 1):
			nCr = factorial(n) // (factorial(r) * factorial(n - r))
			print(nCr, end=" ")
		print(" ")

pascal_triangle()

