# https://www.geeksforgeeks.org/maximum-subarray-size-subarrays-size-sum-less-k/

def bsearch(prefix_sum, n, k):
	left = 0
	right = n
	ans = -1
	while left <= right:
		mid = (left + right) // 2
		for i in range(mid, n + 1):
			curr_val = prefix_sum[i] - prefix_sum[i - mid]
			if curr_val > k:
				i -= 1
				break
		if i == n:
			left = mid + 1
			ans = mid
		else:
			right = mid - 1
	return ans


def max_size(arr, n, k):
	prefix_sum = [0 for i in range(n + 1)]
	for i in range(n):
		prefix_sum[i + 1] = prefix_sum[i] + arr[i]
	return bsearch(prefix_sum, n, k)


# Driver Code
arr = [1, 2, 10, 4]
n = len(arr)
k = 14
print(max_size(arr, n, k))
