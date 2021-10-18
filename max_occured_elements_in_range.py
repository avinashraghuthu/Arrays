#  https://www.geeksforgeeks.org/maximum-occurred-integer-n-ranges/

def max_occured_elements(start_arr, end_arr):
	arr_len = len(start_arr)
	index_arr_len = max(end_arr) + 2
	index_arr = [0 for i in range(index_arr_len)]
	for i in range(arr_len):
		index_arr[start_arr[i]] += 1
		index_arr[end_arr[i]+1] -= 1
	curr_sum = index_arr[0]
	max_occured_element = -1
	for i in range(1, index_arr_len):
		index_arr[i] += index_arr[i-1]
		if curr_sum < index_arr[i]:
			curr_sum = index_arr[i]
			max_occured_element = i
	return max_occured_element
	


L = [1, 4, 9, 13, 21]
# L = [1, 5, 9, 13, 21]
R = [15, 8, 12, 20, 30]

print(max_occured_elements(L, R))