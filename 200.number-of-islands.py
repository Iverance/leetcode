#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands
#
# Medium (34.50%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["11110","11010","11000","00000"]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 11110110101100000000
# Answer: 1
# Example 2:
# 11000110000010000011
# Answer: 3
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m = len(grid)   # rowN
        n = len(grid[0])# colN

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                return
            grid[i] = grid[i][:j] + '0' +grid[i][j+1:]
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        island = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    dfs(row, col)
                    island += 1
        return island
if __name__ == "__main__":
    sol = Solution()
    assert sol.numIslands(["11110","11010","11000","00000"]) == 1
        
