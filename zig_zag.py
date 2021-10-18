#  https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/


def zig_zag(arr):
	arr_len = len(arr)
	flag = True
	for i in range(arr_len-1):
		if flag:
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
		else:
			if arr[i] < arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
		flag = not flag


arr = [4, 3, 7, 8, 6, 2, 1]
zig_zag(arr)
print(arr)
