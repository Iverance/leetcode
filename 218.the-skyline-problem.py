#
# [218] The Skyline Problem
#
# https://leetcode.com/problems/the-skyline-problem
#
# Hard (27.45%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
#
# A city's skyline is the outer contour of the silhouette formed by all the
# buildings in that city when viewed from a distance. Now suppose you are given
# the locations and height of all the buildings as shown on a cityscape photo
# (Figure A), write a program to output the skyline formed by these buildings
# collectively (Figure B).
# 
# 
# 
# ⁠   
# 
# 
# 
# 
# ⁠   
# 
# 
# 
# 
# 
# The geometric information of each building is represented by a triplet of
# integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and
# right edge of the ith building, respectively, and Hi is its height. It is
# guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You
# may assume all buildings are perfect rectangles grounded on an absolutely
# flat surface at height 0.
# 
# For instance, the dimensions of all buildings in Figure A are recorded as: [
# [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
# 
# The output is a list of "key points" (red dots in Figure B) in the format of
# [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key
# point is the left endpoint of a horizontal line segment. Note that the last
# key point, where the rightmost building ends, is merely used to mark the
# termination of the skyline, and always has zero height. Also, the ground in
# between any two adjacent buildings should be considered part of the skyline
# contour.
# 
# For instance, the skyline in Figure B should be represented as:[ [2 10], [3
# 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
# 
# Notes:
# 
# ⁠The number of buildings in any input list is guaranteed to be in the range
# [0, 10000].
# ⁠The input list is already sorted in ascending order by the left x position
# Li. 
# ⁠The output list must be sorted by the x position. 
# ⁠There must be no consecutive horizontal lines of equal height in the output
# skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not
# acceptable; the three lines of height 5 should be merged into one in the
# final output as such: [...[2 3], [4 5], [12 7], ...]
# 
# 
# 
# Credits:Special thanks to @stellari for adding this problem, creating these
# two awesome images and all test cases.
#
class Solution(object):
    """
    Solution: maintain the active heap when sweep buildings' left edge from left to right.
    corner points x =   curr building's right if add curr building,
                        or the tallest building's right edge in active heap if curr building's right is bigger.
    corner points y = 0 if no active building or tallest bulding height in the set
    only add to result when the height change
    """
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        i, n = 0, len(buildings)
        active = []
        res = []
        while i < n or active:
            if not active or i<n and buildings[i][0] <= active[0][1]:
                x = buildings[i][0]
                # handle if buildings at same edge
                while i<n and buildings[i][0] == x:
                    heappush(active, (-buildings[i][2], buildings[i][1]))
                    i+=1
            else:
                x = active[0][1]
                # pop the buildings out that already passed
                while active and active[0][1] <= x:
                    heappop(active)
            y = 0 if not active else -active[0][0]
            if not res or y != res[-1][1]:
                res.append([x,y])
        return res
        """
        O(N^2) solution: height map
        if not buildings:
            return []
        h = [0 for _ in range(0, buildings[-1][1]+1)]
        for b in buildings:
            for i in range(b[0], b[1]+1):
                h[i] = max(h[i], b[2])
        curr = 0
        h.append(0)
        res = []
        for i in range(len(h)-1):
            if h[i] > curr:
                res.append([i, h[i]])
                curr = h[i]
            elif h[i] > h[i+1]:
                res.append([i, h[i+1]])
                curr = h[i+1]
        return res
        """
