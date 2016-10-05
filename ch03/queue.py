import random

# This is an implementation of a queue in Python:
class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)


# Using the childrens game Hot Potato to demonstrate a queue
def hot_potato(name_list, num):
	sim_queue = Queue()
	for name in name_list:
		sim_queue.enqueue(name)
	while sim_queue.size() > 1:
		for i in range(num):
			sim_queue.enqueue(sim_queue.dequeue())
		sim_queue.dequeue()
	return sim_queue.dequeue()

nameList = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]

class Printer:
	def __init__(self, ppm):
		self.page_rate = ppm
		self.current_task = None
		self.time_remaining = 0

	def tick(self):
		if self.current_task != None:
			self.time_remaining = self.time_remaining - 1
			if self.time_remaining <= 0:
				self.current_task = None

	def busy(self):
		if self.current_task != None:
			return True
		else:
			return False

	def start_next(self, new_task):
		self.current_task = new_task
		self.time_remaining = new_task.get_pages() * 60/self.page_rate

class Task:
	def __init__(self, time):
		self.timestamp = time
		self.pages = random.randrange(1,21)

	def get_stamp(self):
		return self.timestamp

	def get_pages(self):
		return self.pages

	def wait_time(self, current_time):
		return current_time - self.timestamp

def simulation(num_seconds, pages_per_minute, num_students):

	lab_printer = Printer(pages_per_minute)
	print_queue = Queue()
	waiting_times = []

	for current_second in range(num_seconds):

		if new_print_task(num_seconds, num_students):
			task = Task(current_second)
			print_queue.enqueue(task)

		if (not lab_printer.busy()) and (not print_queue.is_empty()):
			next_task = print_queue.dequeue()
			waiting_times.append(next_task.wait_time(current_second))
			lab_printer.start_next(next_task)

		lab_printer.tick()

	average_wait = sum(waiting_times) / len(waiting_times)
	print("Average Wait %6.2f secs %3d tasks remaining." %(average_wait, print_queue.size()))

def new_print_task(num_seconds, num_students):
	count = 1 / ((num_students*2)/num_seconds)
	num = random.randrange(1, count+1)
	if num == count:
		return True
	else:
		return False

for i in range(10):
	simulation(3600, 10, 100)









