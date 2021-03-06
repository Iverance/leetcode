#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string
#
# Medium (36.63%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
# 
# Example 1:
# 
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# 
# Example 2:
# 
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# 
# 
# 
# Note:
# 
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
# 
# 
#
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1, n2 = len(s1), len(s2)
        wordCnt = [0 for _ in range(26)]
        for ch in s1:
            wordCnt[ord(ch)-97] += 1

        def check():
            for cnt in wordCnt:
                if cnt != 0:    return False
            return True

        for i in range(n2):
            ch = s2[i]
            wordCnt[ord(ch)-97] -= 1
            if i >= n1:
                prev = s2[i-n1]
                wordCnt[ord(prev)-97] += 1
            if check():   return True
        return False
        
