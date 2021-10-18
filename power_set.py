# https://www.geeksforgeeks.org/power-set/

import math


def subsets(arr):
	arr_len = len(arr)
	power_set_size = int(math.pow(2, arr_len))
	power_set = []
	for counter in range(power_set_size):
		current_list = []
		for j in range(arr_len):
			if counter & (1 << j) > 0:
				current_list.append(arr[j])
		power_set.append(current_list)
	return power_set


print(subsets(['a', 'b', 'c']))
