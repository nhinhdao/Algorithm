class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        - use two pointer 1 -> m and 1-> n
        - compare nums1[m] vs nums2[n]
        - swap small number to big number in nums1
        - increase the pointer that has smaller number
        - continue comparing
        """
        if n == 0: return nums1

        # [ 4,5, >6,4,5,6], m = 3
        # [1,2, 3], n = 3

        # [1,2,2,2,3,5] 3
        # [1,3,5], 3

        end = len(nums1) - 1 # 5
        left = m - 1         # 2
        right = n - 1        # 2

        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]:
                nums1[end] = nums1[left]
                left -=1
            else:
                nums1[end] = nums2[right]
                right -=1
            
            end -= 1

        # left = 3, right = 0

        # i = 0
        while right >= 0:
            nums1[end] = nums2[right]
            right -= 1
            end -= 1
        
        return nums1

test = Solution();

print(test.merge([1,2,2,0,0,0], 3, [1,3,5,6], 3))
print(test.merge([4,5,6,0,0,0], 3, [1,2,3], 3))
