list1 = [0,3,6,7,4,10]
list2 = [5,6,4,3,8,2]

def quadMin(list):
	listMin = list[0]
	steps = 0
	for a in list:
		smallest = True
		for b in list:
			if a > b:
				smallest = False
				steps = steps + 1
		if smallest:
			listMin = a
	print(steps)
	return listMin	

def linearMin(list):
	listMin = list[0]
	steps = 0
	for i in list:
		if i < listMin:
			listMin = i
		steps = steps+1
	print(steps)
	return listMin

print(linearMin(list2))