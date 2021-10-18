# https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form-set-2-o1-extra-space/


def max_min_alternative(arr):
	arr_len = len(arr)
	max_index = arr_len - 1
	min_index = 0
	max_element = arr[max_index] + 1
	for i in range(arr_len):
		if i % 2 == 0:
			arr[i] += (arr[max_index] % max_element) * max_element
			max_index -= 1
		else:
			arr[i] += (arr[min_index] % max_element) * max_element
			min_index += 1
	for i in range(arr_len):
		arr[i] = arr[i] // max_element


arr = [1, 2, 4, 5, 6, 8, 9, 12]
print("Before ", arr)
max_min_alternative(arr)
print("After ", arr)
