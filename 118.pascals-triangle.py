#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle
#
# Easy (38.77%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# 
# For example, given numRows = 5,
# Return
# 
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row += 1,
                else:
                    row += (res[i-1][j-1]+res[i-1][j]),
            res.append(row)
        return res
        
