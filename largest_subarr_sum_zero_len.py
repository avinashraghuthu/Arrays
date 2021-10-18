# https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/

def sub_arr_max_len(arr):
	sum_map = {}
	max_len = 0
	curr_sum = 0
	arr_len = len(arr)
	for i in range(arr_len):
		curr_sum += arr[i]
		
		if curr_sum == 0:
			max_len = i+1
		else:
			if curr_sum in sum_map:
				max_len = max(max_len, i - sum_map[curr_sum])
			else:
				sum_map[curr_sum] = i
	return max_len

arr = [15, -2, 2, -8, 1, 7, 10, 13]
# arr = [1,1,1,1,1,-1,-1]

print(sub_arr_max_len(arr))