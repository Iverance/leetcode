"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        self.m = len(rooms)
        self.n = len(rooms[0])

        for i in range(self.m):
            for j in range(self.n):
                if rooms[i][j] == 0:
                    self.dfs(i, j, 0, rooms)

    def dfs(self, x, y, step, grid):
        if not 0<=x<self.m or not 0<=y<self.n or grid[x][y] == -1 or grid[x][y] < step:
            return

        tmp = min(grid[x][y], step) if grid[x][y] > 0 else grid[x][y]
        grid[x][y] = -1
        self.dfs(x+1,y,step+1, grid)
        self.dfs(x,y+1,step+1, grid)
        self.dfs(x-1,y,step+1, grid)
        self.dfs(x,y-1,step+1, grid)
        grid[x][y] = tmp
