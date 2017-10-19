#
# [79] Word Search
#
# https://leetcode.com/problems/word-search
#
# Medium (26.97%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 
# Given a 2D board and a word, find if the word exists in the grid.
# 
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# 
# For example,
# Given board = 
# 
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
# 
#
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        if not word:
            return True
        wordLen = len(word)
        m=len(board)
        n=len(board[0])
        def dfs(x, y, idx):
            c = board[x][y]
            if c != word[idx]:
                return False
            if idx == wordLen - 1:
                return True
            board[x][y] = '#'
            hasFound = (
                (x > 0 and dfs(x-1,y,idx+1)) or
                (x < m-1 and dfs(x+1,y,idx+1)) or
                (y > 0 and dfs(x,y-1,idx+1)) or
                (y < n-1 and dfs(x,y+1,idx+1))
            )
            board[x][y] = c
            return hasFound

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
        
