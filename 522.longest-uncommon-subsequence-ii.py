#
# [522] Longest Uncommon Subsequence II
#
# https://leetcode.com/problems/longest-uncommon-subsequence-ii
#
# algorithms
# Medium (31.99%)
# Total Accepted:    8.7K
# Total Submissions: 27.3K
# Testcase Example:  '["aba","cdc","eae"]'
#
# 
# Given a list of strings, you need to find the longest uncommon subsequence
# among them. The longest uncommon subsequence is defined as the longest
# subsequence of one of these strings and this subsequence should not be any
# subsequence of the other strings.
# 
# 
# 
# A subsequence is a sequence that can be derived from one sequence by deleting
# some characters without changing the order of the remaining elements.
# Trivially, any string is a subsequence of itself and an empty string is a
# subsequence of any string.
# 
# 
# 
# The input will be a list of strings, and the output needs to be the length of
# the longest uncommon subsequence. If the longest uncommon subsequence doesn't
# exist, return -1.
# 
# 
# Example 1:
# 
# Input: "aba", "cdc", "eae"
# Output: 3
# 
# 
# 
# Note:
# 
# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].
# 
# 
#
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # find is s subsequence of t
        def isSub(s, t):
            t = iter(t)
            return all(c in t for c in s)

        strs.sort(key=len, reverse=True)
        for i in range(len(strs)):
            # check strs[i] is not subsequence of all strings but only itself
            if sum(isSub(strs[i], t) for t in strs) == 1:
                return len(strs[i])
        return -1        
