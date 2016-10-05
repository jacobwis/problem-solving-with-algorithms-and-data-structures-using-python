# This is an implementation of a Stack in Python

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

testString = "This is a test string"


# Use a stack to reverse a string
def revstring(mystr):
	stack = Stack()
	startStr = list(mystr)
	newStr = []
	for c in startStr:
		stack.push(c)
	while not stack.isEmpty():
		newStr.append(stack.pop())
	return "".join(newStr)


# Use a stack to check that parentheses are closed
def parChecker(symbolString):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		index = index + 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

def matches(open, close):
	opens = "([{"
	closers = ")]}"
	return opens.index(open) == closers.index(close)

def divideBy2(decNumber):
	remstack = Stack()

	while decNumber > 0:
		rem = decNumber % 2
		remstack.push(rem)
		decNumber = decNumber // 2

	binString = ""
	while not remstack.isEmpty():
		binString = binString + str(remstack.pop())
	return binString

print(divideBy2(42))
