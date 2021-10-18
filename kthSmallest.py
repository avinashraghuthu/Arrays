#  https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

def partition(arr, low, high):
	pivot = arr[high]
	i = low
	for j in range(low, high):
		if arr[j] < pivot:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[i], arr[high] = arr[high], arr[i]
	return i


def kth_smallest(arr, low, high, k):
	if low <= high:
		index = partition(arr, low, high)
		
		if index == k - 1:
			return arr[index]
		if index > k - 1:
			return kth_smallest(arr, low, index - 1, k)
		return kth_smallest(arr, index + 1, high, k)


arr = [8, 1, 7, 5, 6, 3, 2, 4]
index = kth_smallest(arr, 0, len(arr) - 1, 1)
print(index)
