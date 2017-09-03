#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string
#
# Easy (38.47%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# 
# Example 1:
# Given s = "hello", return "holle".
# 
# 
# 
# Example 2:
# Given s = "leetcode", return "leotcede".
# 
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
#
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lis = list(s)
        vowels = 'aeiouAEIOU'
        l, r = 0, len(s)-1
        while l < r < len(s):
            while l < r and lis[l] not in vowels:
                l += 1
            while l < r < len(s) and lis[r] not in vowels:
                r -= 1
            lis[l], lis[r] = lis[r], lis[l]
            l += 1
            r -= 1
        return "".join(lis)
if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseVowels("hello") == "holle"
    assert sol.reverseVowels("leetcode") == "leotcede"
    assert sol.reverseVowels("hlllf") == "hlllf"
    assert sol.reverseVowels("") == ""
        
