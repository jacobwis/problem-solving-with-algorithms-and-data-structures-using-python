# This is an implementation of an Unordered List in Python, built using a collection of Nodes (see node.py)

from node import Node

class UnorderedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def is_empty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.set_next(self.head)
		self.head = temp
		if temp.get_next() == None:
			self.tail = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.get_next()

		return count

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.get_data() == item:
				found = True
			else:
				current = current.get_next()

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.get_data() == item:
				found = True
			else:
				previous = current
				current = current.get_next()

		if previous == None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

	def append(self, item):
		temp = Node(item)
		if self.tail == None:
			self.tail = temp
		else:
			current = self.tail
			current.set_next(temp)
			self.tail = temp
		return self.tail.get_data()


