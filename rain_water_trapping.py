#  https://www.geeksforgeeks.org/trapping-rain-water/


# Method 1
def trapped_water_with_extra_space(arr):
	arr_len = len(arr)
	left_max = [0] * arr_len
	right_max = [0] * arr_len
	left_max[0] = arr[0]
	for i in range(1, arr_len):
		left_max[i] = max(left_max[i - 1], arr[i])
	
	right_max[arr_len - 1] = arr[arr_len - 1]
	for i in range(arr_len - 2, -1, -1):
		right_max[i] = max(right_max[i + 1], arr[i])
	
	water_trapped = 0
	for i in range(arr_len):
		water_trapped += min(left_max[i], right_max[i]) - arr[i]
	return water_trapped


# Method 2
def trapped_water_no_extra_space(arr):
	arr_len = len(arr)
	low = 0
	high = arr_len - 1
	water_trapped = 0
	left_max = 0
	right_max = 0
	while low <= high:
		if arr[low] < arr[high]:
			if left_max < arr[low]:
				left_max = arr[low]
			else:
				water_trapped += left_max - arr[low]
			low += 1
		else:
			if right_max < arr[high]:
				right_max = arr[high]
			else:
				water_trapped += right_max - arr[high]
			high -= 1
	return water_trapped



arr= [3,0,0,2,0,4]
print(trapped_water_no_extra_space(arr))
print(trapped_water_with_extra_space(arr))