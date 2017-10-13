#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku
#
# Medium (35.70%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]'
#
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# 
# The Sudoku board could be partially filled, where empty cells are filled with
# the character '.'.
# 
# 
# 
# A partially filled sudoku which is valid.
# 
# 
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the
# filled cells need to be validated.
# 
#
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n, m = len(board), len(board[0])
        colMemo = {x:[False for _ in range(m+1)] for x in range(n)}
        sqrMemo = {x:[False for _ in range(m+1)] for x in range(n)}
        for i in range(n):
            rowMemo = [False for _ in range(m+1)]
            for j in range(m):
                if not board[i][j] == '.':
                    val = int(board[i][j])
                    sqrNum = (3 * (j//3)) + i//3
                    if rowMemo[val] or colMemo[j][val] or sqrMemo[sqrNum][val]:
                        return False
                    rowMemo[val] = True
                    colMemo[j][val] = True
                    sqrMemo[sqrNum][val] = True
        return True
