# This is an example of a recursive algorithm used to get the sum of a list

def list_sum(num_list):
	if len(num_list) == 1:
		return num_list[0]
	else:
		return num_list[0] + list_sum(num_list[1:])

print(list_sum([1,3,5,7,9]))
