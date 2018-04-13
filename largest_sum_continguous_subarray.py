#  http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
from sys import maxint


def max_sum_sub_arr(arr, arr_size):
	max_so_far = -maxint -1
	sum_till_now = 0
	start = 0
	end = 0
	s = 0
	for i in xrange(0, arr_size):
		sum_till_now += arr[i]
		if sum_till_now < 0:
			sum_till_now = 0
			s = i+1
		elif max_so_far < sum_till_now:
			max_so_far = sum_till_now
			start = s
			end = i
	return max_so_far, start, end


def test():
	li = [-2, -3, 4, -1, -2, 1, 5, -3]
	max_sum, start, end = max_sum_sub_arr(li, len(li))
	print "max_sum:", max_sum
	print "start:", start
	print "end:", end
