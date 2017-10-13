#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths
#
# Medium (41.37%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# 
# Above is a 3 x 7 grid. How many possible unique paths are there?
# 
# 
# Note: m and n will be at most 100.
#
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for j in range(1,n+1):
            dp[1][j] = 1
        for i in range(1,m+1):
            dp[i][1] = 1
        for i in range(2,m+1):
            for j in range(2,n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
if __name__ == "__main__":
    s = Solution()
    assert s.uniquePaths(1,2) == 1
    assert s.uniquePaths(3,7) == 28    
