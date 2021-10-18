#  http://www.geeksforgeeks.org/equilibrium-index-of-an-array/

#  Number in the array where left and right has equal sum
def equilibrium_point(arr, arr_len):
	total_sum = 0
	left_sum = 0
	equilibrium_index = None
	for i in arr:
		total_sum += i
	right_sum = total_sum
	for i in range(arr_len):
		right_sum -= arr[i]
		if right_sum == left_sum:
			equilibrium_index = i
			break
		left_sum += arr[i]
	if equilibrium_index:
		print(equilibrium_index)
	else:
		print('Not found')


def test():
	arr = [-7, 1, 5, 2, -4, 3, 0]
	equilibrium_point(arr, len(arr))
	
test()