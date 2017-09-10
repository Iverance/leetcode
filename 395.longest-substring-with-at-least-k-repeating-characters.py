#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters
#
# Medium (35.86%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"aaabb"\n3'
#
# 
# Find the length of the longest substring T of a given string (consists of
# lowercase letters only) such that every character in T appears no less than k
# times.
# 
# 
# Example 1:
# 
# Input:
# s = "aaabb", k = 3
# 
# Output:
# 3
# 
# The longest substring is "aaa", as 'a' is repeated 3 times.
# 
# 
# 
# Example 2:
# 
# Input:
# s = "ababbc", k = 2
# 
# Output:
# 5
# 
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is
# repeated 3 times.
# 
# 
#
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        minChr = min(set(s), key=s.count)
        if s.count(minChr) >= k:
            return len(s)
        return max(self.longestSubstring(sub, k) for sub in s.split(minChr))
        
