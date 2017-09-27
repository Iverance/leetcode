#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string
#
# Easy (46.74%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = -1
        m = float('inf')
        for val in d.values():
            if val != -1:
                m = min(m, val)
        return (m, -1)[m == float('inf')]
        
