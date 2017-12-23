#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences
#
# algorithms
# Hard (31.89%)
# Total Accepted:    77.5K
# Total Submissions: 243K
# Testcase Example:  '""\n"a"'
#
# 
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
# 
# 
# 
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
# 
# 
# 
# Here is an example:
# S = "rabbbit", T = "rabbit"
# 
# 
# Return 3.
# 
#
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        """
        s = rabbb
        t = rab
            　t     s
        when rab, rabb: res = "rab, rab"     +   "rab,rab"
                            one ch before       without s[j-1]
        """
        ns, nt = len(s), len(t)
        dp = [[0]*(ns+1) for _  in range(nt+1)]
        dp[0] = [1]*(ns+1)

        for i in range(1, nt+1):
            for j in range(1, ns+1):
                dp[i][j] = dp[i][j-1] + (dp[i-1][j-1] if s[j-1] == t[i-1] else 0)

        return dp[nt][ns]
        
