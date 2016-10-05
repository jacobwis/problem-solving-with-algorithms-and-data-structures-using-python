# This is an example of a recursive algorithm used to convert an Integer to a string representation of any base

def toStr(n, base):
	convertString = "0123456789ABCDEF"
	if n < base:
		return convertString[n]
	else:
		return toStr(n // base, base) + convertString[n % base]

print(toStr(1453, 16))
