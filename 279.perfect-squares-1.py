#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares
#
# Medium (36.95%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
# 
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# 
# 
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
# return 2 because 13 = 4 + 9.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        for s in range(1, int(math.sqrt(n))+1):
            squares.append(s*s)
        squares.reverse()
        level = 0
        q = set([n])

        # BFS, return level when find first 0
        while q:
            qSize = len(q)
            nextq = set()
            for _ in range(qSize):
                num = q.pop()
                if num == 0:
                    return level
                elif num < 0:
                    continue
                for sq in squares:
                    nextq.add(num - sq)
            q = nextq
            level+=1
        
