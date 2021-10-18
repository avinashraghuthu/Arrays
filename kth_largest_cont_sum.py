#  https://www.geeksforgeeks.org/k-th-largest-sum-contiguous-subarray/
import heapq


def kthLargestSum(arr, arr_len, k):
    sum_arr = []
    sum_arr.append(0)
    sum_arr.append(arr[0])
    min_heap = []
    for i in range(2, arr_len + 1):
        sum_arr.append(sum_arr[i - 1] + arr[i - 1])
    for i in range(1, arr_len + 1):
        for j in range(i, arr_len + 1):
            curr_sum = sum_arr[j] - sum_arr[i - 1]
            if len(min_heap) < k:
                heapq.heappush(min_heap, curr_sum)
            elif min_heap[0] < curr_sum:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, curr_sum)
    return min_heap[0]


#  Driver program to test above function
a = [10, -10, 20, -40]
n = len(a)
k = 6

# calls the function to find out the
# k-th largest sum
print(kthLargestSum(a, n, k))
