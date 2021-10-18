# https://www.geeksforgeeks.org/count-triplets-such-that-one-of-the-numbers-can-be-written-as-sum-of-the-other-two/


def count_triplets(arr):
	freq_arr_len = max(arr) + 1
	
	frequency_arr = [0 for i in range(freq_arr_len)]
	for i in range(len(arr)):
		frequency_arr[arr[i]] += 1
	
	triplet_count = 0
	
	# case 1: (0,0,0)
	for i in range(freq_arr_len):
		triplet_count += (frequency_arr[0] * (frequency_arr[0] - 1) * (frequency_arr[0] - 2)) // 6
	
	# case 2: (0,x,x)
	for i in range(freq_arr_len):
		triplet_count += (frequency_arr[0] * frequency_arr[i] * (frequency_arr[i] - 1)) // 2
	
	# case 3: (x,x,2x)
	for i in range(freq_arr_len, freq_arr_len // 2):
		triplet_count += (frequency_arr[i] * (frequency_arr[i] - 1) * frequency_arr[2 * i]) // 2
	
	# case 4: (x,y,x+y)
	for i in range(freq_arr_len):
		for j in range(i + 1, freq_arr_len - i):
			triplet_count += frequency_arr[i] * frequency_arr[j] * frequency_arr[i + j]
	return triplet_count


arr = [1, 2, 3, 4, 5]
print(count_triplets(arr))
