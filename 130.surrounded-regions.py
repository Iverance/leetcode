#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions
#
# Medium (18.50%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["XXXX","XOOX","XXOX","XOXX"]'
#
# 
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# 
# 
# For example,
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 
# 
# After running your function, the board should be:
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
#
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        m = len(board)
        n = len(board[0])
        queue = []
        
        for row in range(m):
            if board[row][0] == 'O':
                queue.append([row, 0])
            if board[row][n-1] == 'O':
                queue.append([row, n-1])
        for col in range(n):
            if board[0][col] == 'O':
                queue.append([0, col])
            if board[m-1][col] == 'O':
                queue.append([m-1, col])
        while queue:
            i, j = queue.pop(0)
            if not (0<=i<m) or not (0<=j<n) or board[i][j] != 'O':
                continue
            board[i][j] = '1'
            queue.append([i+1, j])
            queue.append([i, j+1])
            queue.append([i-1, j])
            queue.append([i, j-1])
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '1':
                    board[i][j] = 'O'

if __name__ == "__main__":
    sol = Solution()
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    sol.solve(board)
    print(board)        
