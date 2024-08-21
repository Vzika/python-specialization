#when passing an arg in a functon
#normal args first, followed by arbituary positional argument(*args), the followew
#by arbituary keyword argument(**kwargs) else their will be an erro

#in args the aruments are collected as a tuple, they are no mutable ie it cannot be changed
#in kwargs the arg are collect as dictionary, and can be accesed using a key,value pair


# normal arg, u cant pass more than 2 argument
def add(a, b):

	sum = a+b
	print(sum)

add(5,10)

#*arg, you can pass more than 2 arguments


def summing(*numbers):
	count =0
	for num in numbers:
		count = count + num
	print(count)

summing(2,3,4,5,6) 


# **kwargs

def info_people(**kwargs):

	for key, val in kwargs.items():
		print(key, val)


info_people(name = "zika", age = "20", town=  "abuja")


