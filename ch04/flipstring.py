# This is a self check exercise in chapter 4 of the book
# 
# Problem: Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string

def flip_string(string):
	if len(string) == 1:
		return string[0]
	else:
		return flip_string(string[1:]) + string[0]


print(flip_string("T"))	