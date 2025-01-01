class Solution(object):
    def __init__(self, target):
        self.target = target

    def guess(self, num):
        return -1 if num > self.target else 1 if num < self.target else 0
    
    def guessNumber(self, n):
        left = 1
        right = n

        while left <= right:
            # find the middle number
            num = (left + right) // 2

            if self.guess(num) == -1:
                right =  num - 1
            elif self.guess(num) == 1:
                left = num + 1
            else: 
                return num
        
        return None
    

test = Solution(7)
print(test.guessNumber(10))