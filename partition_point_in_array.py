#  http://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/


def partition_point(arr, arr_len):
	left_max = []
	left_max.append(arr[0])

	for i in range(1, arr_len):
		left_max.insert(i, max(left_max[i-1], arr[i-1]))

	i = arr_len - 1
	right_min = arr[i]
	while i >= 0:
		if (arr[i] > left_max[i]) and arr[i] < right_min:
			return i
		right_min = min(right_min, arr[i])
		i -= 1
	return -1


def test():
	arr=[5, 1, 4, 3, 6, 8, 10, 7, 9]
	print("Index of element: ", partition_point(arr, len(arr)))