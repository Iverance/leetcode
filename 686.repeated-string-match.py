#
# [686] Repeated String Match
#
# https://leetcode.com/problems/repeated-string-match
#
# algorithms
# Easy (32.28%)
# Total Accepted:    9.1K
# Total Submissions: 28.2K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# Given two strings A and B, find the minimum number of times A has to be
# repeated such that B is a substring of it. If no such solution, return -1.
# 
# 
# For example, with A = "abcd" and B = "cdabcdab". 
# 
# 
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a
# substring of it; and B is not a substring of A repeated two times
# ("abcdabcd").
# 
# 
# Note:
# The length of A and B will be between 1 and 10000.
# 
#
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        n = len(B)
        cnt = 1
        repeat = A
        while len(repeat) < n:
            repeat += A
            cnt += 1
        if B in repeat:
            return cnt
        if B in repeat+A:
            return cnt + 1
        return -1
        
