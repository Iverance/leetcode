#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome
#
# Easy (26.33%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""'
#
# 
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# 
# 
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# 
# 
# 
# Note:
# Have you consider that the string might be empty? This is a good question to
# ask during an interview.
# 
# For the purpose of this problem, we define empty string as valid palindrome.
# 
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join([x for x in list(s.lower()) if x in "0123456789" or 96<ord(x)<123 or 64<ord(x)<91])
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True
