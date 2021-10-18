def partition(arr, low, high):
	pivot = arr[high]
	i = low
	for j in range(low, high):
		if arr[j] < pivot:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[i], arr[high] = arr[high], arr[i]
	return i


def quicksort(arr, low, high):
	if low < high:
		pivot_index = partition(arr, low, high)
		
		quicksort(arr, low, pivot_index - 1)
		quicksort(arr, pivot_index + 1, high)


arr = [8, 1, 7, 5, 6,8, 3, 2, 4, 8]
# arr = [10,80,30,70,40,50,70]

quicksort(arr, 0, len(arr) - 1)
print(arr)
