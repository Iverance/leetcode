#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix
#
# Hard (36.57%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an integer matrix, find the length of the longest increasing path.
# 
# 
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
# 
# 
# Example 1:
# 
# nums = [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ]
# 
# 
# 
# 
# Return 4
# 
# The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# nums = [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ]
# 
# 
# 
# 
# Return 4
# 
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not
# allowed.
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:  return 0
        m = len(matrix)
        n = len(matrix[0])
        memo = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        maxLen = 0
        def dfs(x,y):
            if memo[x][y] != 0:
                return memo[x][y]
            wrapMax = 1
            for offsetX, offsetY in directions:
                i, j = x + offsetX, y+offsetY
                if i<0 or j<0 or i>m-1 or j>n-1:    continue
                if matrix[x][y] < matrix[i][j]:
                    wrapMax = max(wrapMax,dfs(i,j)+1)
            memo[x][y] = wrapMax
            return wrapMax

        for i in range(m):
            for j in range(n):
                maxLen = max(maxLen, dfs(i,j))
        return maxLen
        """
        def dfs(i,j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1+max(
                dfs(i-1,j) if i and val>matrix[i-1][j] else 0,
                dfs(i+1,j) if i<M-1 and val>matrix[i+1][j] else 0,
                dfs(i,j-1) if j and val>matrix[i][j-1] else 0,
                dfs(i,j+1) if j<N-1 and val>matrix[i][j+1] else 0)
            return dp[i][j]
        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0]*N for _ in xrange(M)]
        return max(dfs(i,j) for i in range(M) for j in range(N))
        """
if __name__ == "__main__":
    s = Solution()
    assert s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]) == 4
    assert s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]) == 4
