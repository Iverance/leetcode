#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix
#
# Medium (26.17%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# 
# 
# For example,
# Given the following matrix:
# 
# 
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# 
# You should return [1,2,3,6,9,8,7,4,5].
# 
#
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = []
        if not matrix:
            return r
        n = len(matrix)
        m = len(matrix[0])
        rowStart, rowEnd = 0, n-1
        colStart, colEnd = 0, m-1
        i, j = 0, 0
        while rowStart <= rowEnd and colStart <= colEnd:
            # right
            for j in range(colStart, colEnd+1):
                r.append(matrix[rowStart][j])
            rowStart += 1

            # Down
            for i in range(rowStart, rowEnd+1):
                r.append(matrix[i][colEnd])
            colEnd -= 1

            # left
            if rowStart <= rowEnd:
                for j in range(colEnd, colStart-1, -1):
                    r.append(matrix[rowEnd][j])
                rowEnd -= 1

            # up
            if colStart <= colEnd:
                for i in range(rowEnd, rowStart-1, -1):
                    r.append(matrix[i][colStart])
                colStart += 1

        return r
        
