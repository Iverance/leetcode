#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter
#
# algorithms
# Easy (57.50%)
# Total Accepted:    61.6K
# Total Submissions: 107.2K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water. Grid cells are connected
# horizontally/vertically (not diagonally). The grid is completely surrounded
# by water, and there is exactly one island (i.e., one or more connected land
# cells). The island doesn't have "lakes" (water inside that isn't connected to
# the water around the island). One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
# 
# Example:
# 
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
#
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    perimeter += 4
                    if i > 0:
                        perimeter -= grid[i-1][j]
                    if i < m-1:
                        perimeter -= grid[i+1][j]
                    if j > 0:
                        perimeter -= grid[i][j-1]
                    if j < n-1:
                        perimeter -= grid[i][j+1]
        return perimeter
        
