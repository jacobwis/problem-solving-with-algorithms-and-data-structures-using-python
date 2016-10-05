# This is an example of a recursive algorithm used to find out if a string is a panindrome
def is_pal(string):
	if len(string) <= 2:
		return True
	else: 
		return (string[0] == string[-1]) and is_pal(string[1:-1])


print(is_pal("raddsar"))