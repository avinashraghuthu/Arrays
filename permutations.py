def permutations(input_str):
	permutations_utils(list(input_str), 0, len(input_str)-1)
	
	
def permutations_utils(str_arr, left_index, right_index):
	if left_index == right_index:
		print("".join(str_arr))
	else:
		for i in range(left_index, right_index+1):
			str_arr[i], str_arr[left_index] = str_arr[left_index], str_arr[i]
			permutations_utils(str_arr, left_index+1, right_index)
			str_arr[i], str_arr[left_index] = str_arr[left_index], str_arr[i]


input_str = 'ABC'
permutations(input_str)
