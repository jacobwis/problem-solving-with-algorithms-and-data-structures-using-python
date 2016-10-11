# Implementation of an ordered sequential search algorithm in Python

def ordered_sequential_search(a_list, item):
	pos = 0
	found = False
	stop = False

	while pos < len(a_list) and not found and not stop:
		if a_list[pos] == item:
			found = True
		else:
			if a_list[pos] > item:
				stop = True
			else:
				pos = pos+1

	return found

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list, 13))