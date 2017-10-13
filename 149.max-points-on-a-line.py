#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line
#
# Hard (15.29%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
#
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def getGCD(self,x,y):
        if y == 0:
            return x
        return self.getGCD(y, x%y)
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        n = len(points)
        ans = 0
        for i in range(n):
            p1 = points[i]
            slope = {}
            cntSame, maxS = 0, 0
            for j in range(i+1, n):
                p2 = points[j]
                dx = p1.x - p2.x
                dy = p1.y - p2.y
                if dx == 0 and dy == 0:
                    cntSame += 1
                else:
                    gcd = self.getGCD(dx,dy)
                    s = (dx//gcd, dy//gcd)
                    if s not in slope:
                        slope[s] = 0
                    slope[s] += 1
                    maxS = max(slope[s],maxS)
            ans = max(ans,maxS+cntSame+1)
        return ans
