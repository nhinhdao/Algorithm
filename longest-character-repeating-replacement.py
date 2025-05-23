class Solution(object):
    def characterReplacement(self, s, k):
        """
        You are given a string s and an integer k.
        You can choose any character of the string and change it to any other uppercase English character. 
        You can perform this operation at most k times.
        s = "AABABBA", k = 1 longest 4
        s = "ABAB", k = 2, longest 4
        add each charactor to hash {A: 1; B: 4}
        max length is the char with the most count 3, k = 2, length = 5
        """
        chars = {}
        max_length = 0
        left = 0
        chars[s[right]] = chars.get(s[right], 0) + 1

        for right in range(len(s)):
            max_length = max(max_length, chars[s[right]])

            print("before ", s[left:right+1])
            while k < right - left + 1 - max_length:
                chars[s[left]] -= 1
                left += 1
            print("after ", s[left:right+1])
        
        return right - left + 1
    
test = Solution()
test.characterReplacement("AABABBA", 1)
