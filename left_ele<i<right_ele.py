# https://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/


def find_element(arr):
	arr_len = len(arr)
	left_max = [0] * arr_len
	left_max[0] = arr[0]
	for i in range(1, arr_len):
		left_max[i] = max(left_max[i-1], arr[i-1])
	
	right_min = [0] * arr_len
	right_min[arr_len - 1] = arr[arr_len - 1]
	for i in range(arr_len -2, -1, -1):
		right_min[i] = min(right_min[i+1], arr[i+1])
	
	for i in range(arr_len):
		if left_max[i] < arr[i] < right_min[i]:
			return i
		
	return -1


arr = [5, 1, 4, 3, 6, 8, 10, 11, 12]
print("Index of the element is", find_element(arr))
