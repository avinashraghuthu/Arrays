# https://www.geeksforgeeks.org/k-maximum-sum-combinations-two-arrays/

import heapq

def kMaxSumComb(arr1, arr2, k):
    arr_len = len(arr1)
    arr1.sort()
    arr2.sort()
    min_heap = []
    index_set = set()
    index_set.add((arr_len-1, arr_len-1))
    min_heap.append((arr1[arr_len-1]+arr2[arr_len-1], (arr_len-1, arr_len-1)))
    for i in range(k):
        curr_sum = min_heap.pop()
        print(curr_sum[0])
        arr1_index = curr_sum[1][0]
        arr2_index = curr_sum[1][1]
        index_tuple = (arr1_index-1, arr2_index)
        if index_tuple not in index_set:
            next_sum = arr1[arr1_index-1]+arr2[arr2_index]
            min_heap.append((next_sum, index_tuple))
            index_set.add(index_tuple)
            
        index_tuple = (arr1_index, arr2_index-1)
        if index_tuple not in index_set:
            next_sum = arr1[arr1_index]+arr2[arr2_index-1]
            min_heap.append((next_sum, index_tuple))
            index_set.add(index_tuple)
        heapq.heapify(min_heap)
    return min_heap
    

arr1 = [1, 4, 2, 3 ]
arr2= [2, 5, 1, 6]

kMaxSumComb(arr1, arr2, 4)