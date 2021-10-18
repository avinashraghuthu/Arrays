#  https://www.geeksforgeeks.org/arrange-given-numbers-form-biggest-number-set-2/


def largest_number(arr):
	max_number_len = len(str(max(arr)))
	
	modified_arr = []
	for arr_ele in arr:
		temp = str(arr_ele) * max_number_len
		modified_arr.append((temp[:max_number_len], str(arr_ele)))
	
	modified_arr.sort(reverse=True)
	max_number = ''
	
	for arr_ele_tuple in modified_arr:
		max_number += arr_ele_tuple[1]
	return max_number


# arr = [22, 9, 54, 67]
arr = [1, 34, 3, 98, 9, 76, 45, 4, 12, 121]
print(largest_number(arr))
