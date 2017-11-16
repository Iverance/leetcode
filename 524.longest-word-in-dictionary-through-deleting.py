#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting
#
# algorithms
# Medium (43.14%)
# Total Accepted:    14.9K
# Total Submissions: 34.6K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.
# 
# Example 1:
# 
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# Output: 
# "apple"
# 
# 
# 
# 
# Example 2:
# 
# Input:
# s = "abpcplea", d = ["a","b","c"]
# 
# Output: 
# "a"
# 
# 
# 
# Note:
# 
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
# 
# 
#
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        """
        Time: O(len(s)*len(d)*log[len(d)])
        """
        d = sorted(d, key=lambda x:(-len(x), x))
        for word in d:
            i, n = 0, len(word)
            for ch in s:
                if i < n and ch == word[i]:
                    i+=1
            if i == n:
                return word
        return ""
