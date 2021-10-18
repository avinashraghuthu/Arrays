# https://afteracademy.com/blog/operations-on-heaps

def min_heapify(arr, index, arr_size):
	left_child_index = 2 * index + 1
	right_index_index = 2 * index + 2
	smallest = index
	if left_child_index < arr_size and arr[left_child_index] < arr[index]:
		smallest = left_child_index
	if right_index_index < arr_size and arr[right_index_index] < arr[smallest]:
		smallest = right_index_index
	if smallest != index:
		arr[index], arr[smallest] = arr[smallest], arr[index]
		min_heapify(arr, smallest, arr_size)


def build_min_heap(arr, arr_size):
	index = (arr_size - 1) // 2
	while index >= 0:
		min_heapify(arr, index, arr_size)
		index -= 1


arr = [8, 6, 7, 5, 1, 3, 2, 4]
build_min_heap(arr, len(arr))
print(arr)
