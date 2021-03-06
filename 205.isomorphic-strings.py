#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings
#
# Easy (33.90%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# For example,
# Given "egg", "add", return true.
# 
# Given "foo", "bar", return false.
# 
# Given "paper", "title", return true.
# 
# Note:
# You may assume both s and t have the same length.
#
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sl = len(s)
        tl = len(t)
        if sl != tl:
            return False
        table = {}
        for i in range(sl):
            if s[i] not in table:
                table[s[i]] = t[i]
            else:
                if table[s[i]] != t[i]: return False
        table = {}
        for i in range(tl):
            if t[i] not in table:
                table[t[i]] = s[i]
            else:
                if table[t[i]] != s[i]: return False
        return True
        
