# https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/

def sub_arr_with_equal_0_1(arr):
	arr_len = len(arr)
	sum_map = {}
	curr_sum = 0
	end_index = -1
	max_len = 0
	for i in range(arr_len):
		if arr[i] == 0:
			curr_sum += -1
		else:
			curr_sum += 1
		if curr_sum == 0:
			max_len = i + 1
			end_index = i
		else:
			if curr_sum in sum_map:
				max_len = max(max_len, i - sum_map[curr_sum])
				end_index = i
			else:
				sum_map[curr_sum] = i
	if end_index != -1:
		print("start index:", end_index - max_len + 1)
		print("end index:", end_index)
	else:
		print("Not found")


arr = [1, 1, 1, 1, 1, 0, 0]
# arr = [1, 0, 0, 1, 0, 1, 1]
sub_arr_with_equal_0_1(arr)
