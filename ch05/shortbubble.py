# A bubble sort algorithm in python that can recognize if a list is sorted before its made n-1 passes, and stop early.

def short_bubble_sort(a_list):
	exchanges = True
	pass_num = len(a_list) - 1
	while pass_num > 0 and exchanges:
		exchanges = False
		for i in range(pass_num):
			if a_list[i] > a_list[i + 1]:
				exchanges = True
				temp = a_list[i]
				a_list[i] = a_list[i + 1]
				a_list[i + 1] = temp
				pass_num = pass_num - 1

a_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
short_bubble_sort(a_list)
print(a_list)				