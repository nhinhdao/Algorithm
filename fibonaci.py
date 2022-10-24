class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

    def fibNoRecursive(self, n):
        """
        0 1 1 2 3 5 8 13
        start with 0 and 1;
        pre = 0
        next = 1
        index = 2
        sum = 0
        while index <= n:
            sum = pre + next
            pre = next
            next = sum
            index += 1 
        
        return sum
        """
        pre = 0
        next = 1
        if n == 0:
            return pre
        if n == 1:
            return next

        index = 2
        sum = 0
        while index <= n:
            sum = pre + next
            pre = next
            next = sum
            index += 1 
        
        return sum

test = Solution()
print(test.fib(6))
print(test.fibNoRecursive(6))