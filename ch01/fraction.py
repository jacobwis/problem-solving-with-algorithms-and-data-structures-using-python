def gcd(m,n):
	while m%n != 0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm%oldn
	return n

def getNum(self):
	return self.num

def getDen(self):
	return self.den


class Fraction:
	def __init__(self,top,bottom):
		common = gcd(top,bottom)
		self.num = top//common
		self.den = bottom//common

	def __str__(self):
		return str(self.num)+"/"+str(self.den)

	def show(self):
		print(self.num,"/",self.den)

	def __add__(self,otherfraction):
		newnum = self.num*otherfraction.den + \
					self.den*otherfraction.num
		newden = self.den * otherfraction.den
		return Fraction(newnum,newden)

	def __sub__(self,otherfraction):
		newnum = self.num*otherfraction.den - \
					self.den*otherfraction.num
		newden = self.den * otherfraction.den
		return Fraction(newnum,newden)

	def __mul__(self,otherfraction):
		newnum = self.num*otherfraction.num
		newden = self.den*otherfraction.den
		return Fraction(newnum,newden)

	def __div__(self,otherfraction):
		newnum = self.num*otherfraction.den
		newden = self.den*otherfraction.num
		return Fraction(newnum,newden)

	def __eq__(self, other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum == secondnum

	def __gt__(self,other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum > secondnum

	def __ge__(self,other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum >= secondnum	

	def __lt__(self,other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum < secondnum

	def __le__(self,other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum <= secondnum

	def __ne__(self,other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum != secondnum

x = Fraction(1,2)
y = Fraction(2,4)
print(x>y) 
# false
print(x>=y)
# true
print(x<y)
# false
print(x<=y)
# true
print(x!=y)
# false















