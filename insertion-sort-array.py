class Solution(object):
    pass
    def sortArray(self, nums):
        for i in range (1, len(nums)):
            j = i - 1
            while (j >= 0 and nums[i] < nums[j]):
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1
                i -= 1
        return nums


test = Solution()
print(test.sortArray([2,5,3,1]))