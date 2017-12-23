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
from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        m = len(rooms)
        n = len(rooms[0])
        MAX_INF = 2147483647
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.appendleft((i,j))
                    
        while len(q):
            i, j = q.pop()
            if i > 0 and rooms[i-1][j] == MAX_INF:
                rooms[i-1][j] = rooms[i][j] + 1
                q.appendleft((i-1,j))
            if i < m-1 and rooms[i+1][j] == MAX_INF:
                rooms[i+1][j] = rooms[i][j] + 1
                q.appendleft((i+1,j))
            if j > 0 and rooms[i][j-1] == MAX_INF:
                rooms[i][j-1] = rooms[i][j] + 1
                q.appendleft((i,j-1))
            if j < n-1 and rooms[i][j+1] == MAX_INF:
                rooms[i][j+1] = rooms[i][j] + 1
                q.appendleft((i,j+1))
