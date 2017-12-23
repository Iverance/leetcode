"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""
class cell(object):
    def __init__(self):
        self.up = self.left = 0
        self.down = self.right = 0
    def enemyCount(self):
        return sum([self.up, self.down, self.left, self.right])

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[cell() for _ in range(n)] for _ in range(m)]
        res = 0
        # Count enemies from top-left to bot-right
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue
                dp[i][j].up = (0 if i == 0 else dp[i-1][j].up) + (grid[i][j] == 'E')
                dp[i][j].left = (0 if j == 0 else dp[i][j-1].left) + (grid[i][j] == 'E')
        # Count enemies from bot-right to top-left
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j] == 'W':
                    continue
                dp[i][j].down = (0 if i == m-1 else dp[i+1][j].down) + (grid[i][j] == 'E')
                dp[i][j].right = (0 if j == n-1 else dp[i][j+1].right) + (grid[i][j] == 'E')
                # Place bomb at empty cell
                if grid[i][j] == '0':
                    res = max(res, dp[i][j].enemyCount())
        return res
