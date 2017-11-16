#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow
#
# algorithms
# Medium (33.98%)
# Total Accepted:    19.5K
# Total Submissions: 57.3K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# Example:
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 
#
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        memo = [[0 for _ in range(n)] for _ in range(m)]
        res = []
        # flow 1: Pac, 2: Alt 3: both
        def dfs(x,y,flow,preHeight):
            # return if out-of bound
            if not 0<=x<m or not 0<=y<n or preHeight > matrix[x][y]:
                return
            # return if traverse already for same flow
            if memo[x][y] == flow or memo[x][y] > 2:
                return
            memo[x][y] += flow
            if memo[x][y] == 3:
                res.append([x,y])
            dfs(x+1,y,flow,matrix[x][y])
            dfs(x,y+1,flow,matrix[x][y])
            dfs(x-1,y,flow,matrix[x][y])
            dfs(x,y-1,flow,matrix[x][y])

        for i in range(m):
            dfs(i, n-1, 2, matrix[i][n-1])
            dfs(i, 0, 1, matrix[i][0])
        for j in range(n):
            dfs(m-1, j, 2, matrix[m-1][j])
            dfs(0, j, 1, matrix[0][j])
        # for m in memo:
        #     print(m)

        return res
        
