# This is programming exercise 5 from chapter 3.
# 
# "Implement the queue ADT, using a list such that the rear of the queue is at the end of the list"
# 
# Solution: Since I already created a queue data type (see queue.py), 
# this is as simple as taking that code and modifying the enqueue and dequeue operations 
# so that enqueueing an item adds it to the end of the list and 
# dequeueing an item takes it from the beginning


class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

def test():		
	q = Queue()
	q.enqueue(10)
	q.enqueue(12)
	q.enqueue(18)
	q.enqueue(4)

	# Should return 10
	print(q.dequeue())