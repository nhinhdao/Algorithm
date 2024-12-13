"""
climb n stairs using 1 or 2 steps
1. simple input using 1 or 2 steps
    n = 1:  1 --- 1 way 0 + 1

    n = 2:  2
            1 + 1 --- 2 ways 2 + 1
    n = 3:  2 + 1
            1 + 2
            1 + 1 + 1 --- 3 ways 2 + 1
    n = 4:  2 + 2 
            2 + 1 + 1 
            1 + 2 + 1  
            1 + 1 + 2
            1 + 1 + 1 + 1  --- 5 ways 4 + 1

    n = 5:  2 + 2 + 1                    
            2 + 1 + 2
            1 + 2 + 2               --- 3 ways to use 2 2s
            2 + 1 + 1 + 1
            1 + 2 + 1 + 1
            1 + 1 + 2 + 1
            1 + 1 + 1 + 2           --- 4 ways to use 1 2s
            1 + 1 + 1 + 1 + 1       --- 1 ways 0 2s === 8 ways

    n = 6:  2 + 2 + 2               --- 1 ways use 3 2s
            2 + 2 + 1 + 1
            2 + 1 + 2 + 1
            2 + 1 + 1 + 2
            1 + 2 + 2 + 1
            1 + 2 + 1 + 2           
            1 + 1 + 2 + 2           --- 6 ways to use 2 2s
            2 + 1 + 1 + 1 + 1
            1 + 2 + 1 + 1 + 1
            1 + 1 + 2 + 1 + 1
            1 + 1 + 1 + 2 + 1
            1 + 1 + 1 + 1 + 2       --- 5 ways to use 1 2s
            1 + 1 + 1 + 1 + 1 + 1   --- 1 ways to use 0 2s ==== 13 ways
2. pattern 
Follow fibonaci numbers

"""

class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        if n == 2: return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    def climbStairsNorecursive(self, n):
        pre = 1
        next = 2
        if n == 1:
            return pre
        if n == 2:
            return next

        index = 3
        sum = 0
        while index <= n:
            sum = pre + next
            pre = next
            next = sum
            index += 1 
        
        return sum

test = Solution()
print(test.climbStairs(38))
print(test.climbStairsNorecursive(38))