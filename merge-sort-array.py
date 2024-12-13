class Solution(object):
    def sortArray(self, nums):
        if len(nums) > 1:
            midIndex = len(nums)//2
            leftHalf = nums[:midIndex]
            rightHalf = nums[midIndex:]

            self.sortArray(leftHalf)
            self.sortArray(rightHalf)

            i = j = k = 0

            while (i < len(leftHalf) and j < len(rightHalf)):
                if (leftHalf[i] < rightHalf[j]):
                    nums[k] = leftHalf[i]
                    i += 1
                else:
                    nums[k] = rightHalf[j]
                    j += 1
                k += 1

            while i < len(leftHalf):
                nums[k] = leftHalf[i]
                i += 1
                k += 1
            
            while j < len(rightHalf):
                nums[k] = rightHalf[j]
                j += 1
                k += 1

        return nums


test = Solution()
print(test.sortArray([5,3, 1, 2]))