#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string
#
# Easy (59.24%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and returns the string
# reversed.
# 
# 
# Example:
# Given s = "hello", return "olleh".
# 
#
class Solution(object):
    def reverseString1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        n = len(s)
        l = list(s)
        left = 0
        right = n - 1
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
        return "".join(l)
    def reverseString1(self, s):
        return s[::-1]
        
