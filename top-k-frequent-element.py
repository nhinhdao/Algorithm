from ast import List
import heapq


class Solution:
    def topKPrequentElement(nums, k):
        if k == len(nums):
            return nums

        result = {}
        for x in nums:
            result[x] = 1 + result.get(x, 0)
        # equivalent to result = Counter(nums)
        # Counter from collections class keeps track of element and its count

        return heapq.nlargest(k, result.keys(), key=result.get)
    print(topKPrequentElement([1,1,1,2,2,3], 2));


# [2, 6, 5, 4, 8] 3 
