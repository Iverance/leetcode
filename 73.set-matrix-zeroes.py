#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes
#
# Medium (35.93%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[0]]'
#
# 
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in place.
# 
# 
# click to show follow up.
# 
# Follow up:
# 
# 
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# 
# 
#
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        firstRowZero = firstColZero = False
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    firstRowZero = True if i == 0 else firstRowZero
                    firstColZero = True if j == 0 else firstColZero
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] and (matrix[0][j] == 0 or matrix[i][0] == 0):
                    matrix[i][j] = 0
        if firstRowZero:
            matrix[0] = [0] * col
        if firstColZero:
            for i in range(row):
                matrix[i][0] = 0
        print(matrix)
if __name__ == "__main__":
    sol = Solution()
    sol.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])
