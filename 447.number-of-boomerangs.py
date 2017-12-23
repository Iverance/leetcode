#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs
#
# algorithms
# Easy (45.77%)
# Total Accepted:    29.9K
# Total Submissions: 65.3K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
# 
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
# 
# Example:
# 
# Input:
# [[0,0],[1,0],[2,0]]
# 
# Output:
# 2
# 
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
# 
# 
#
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        table = collections.defaultdict(int)
        n = len(points)
        ans = 0
        def getDistance(p1, p2):
            return abs(p1[0] - p2[0])**2 + abs(p1[1] - p2[1])**2

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                d = getDistance(points[i], points[j])
                table[d] += 1

            for d in table:
                val = table[d]
                ans += val * (val-1)
            table = collections.defaultdict(int)
        return ans
        
