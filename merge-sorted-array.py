class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        - since the two arrays are sorted, we look at last number of each array
        - use two pointers m - 1 and n - 1 to loop thru 2 arrays, start at the last indexes
        - use a pointer = last index of (m + n) - 1 to 
        - compare nums1[m] vs nums2[n]
        - set the bigger number index[end] of nums1, decrease end each time
        - append any left over number from nums2 to nums1
        """
        if n == 0: return nums1

        end = (m+n) - 1 
        left = m - 1         
        right = n - 1        

        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]:
                nums1[end] = nums1[left]
                left -=1
            else:
                nums1[end] = nums2[right]
                right -=1
            
            end -= 1

        while right >= 0:
            nums1[end] = nums2[right]
            right -= 1
            end -= 1
        
        return nums1

test = Solution();

print(test.merge([1,2,2,0,0,0], 3, [1,3,5,6], 3))
print(test.merge([4,5,6,0,0,0], 3, [1,2,3], 3))
