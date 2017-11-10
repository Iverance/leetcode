#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word
#
# Easy (31.88%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# 
# Example:
# 
# Input: "Hello World"
# Output: 5
# 
# 
#
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        cnt = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                break
            cnt+=1
        return cnt
        
