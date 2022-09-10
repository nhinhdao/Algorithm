def getConcatenation(nums):
        count = len(nums)
        ans = [0] * (count * 2)
        n = 0
        
        while n < count:
            ans[n] = ans[n + count] = nums[n]
            n += 1
            
        return ans


print(getConcatenation([1,2,1]))