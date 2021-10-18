#  https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/

import math


def triplet(arr):
	arr_len = len(arr)
	for i in range(arr_len):
		arr[i] = arr[i]* arr[i]
	
	arr.sort()
	
	for c_index in range(arr_len-1,1,-1):
		b_index = c_index -1
		a_index = 0
		while a_index < b_index:
			if arr[a_index] + arr[b_index] == arr[c_index]:
				print("a: ", int(math.sqrt(arr[a_index])), " b: ", int(math.sqrt(arr[b_index])), " c: ", int(math.sqrt(arr[c_index])))
				return
			elif arr[a_index] + arr[b_index] < arr[c_index]:
				a_index += 1
			else:
				b_index -= 1
			
	print("Nothing found")


arr = [3, 1, 4, 6, 5]
triplet(arr)
