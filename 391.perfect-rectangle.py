#
# [391] Perfect Rectangle
#
# https://leetcode.com/problems/perfect-rectangle
#
# algorithms
# Hard (26.98%)
# Total Accepted:    11.9K
# Total Submissions: 44K
# Testcase Example:  '[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]'
#
# 
# Given N axis-aligned rectangles where N > 0, determine if they all together
# form an exact cover of a rectangular region.
# 
# 
# 
# Each rectangle is represented as a bottom-left point and a top-right point.
# For example, a unit square is represented as [1,1,2,2]. (coordinate of
# bottom-left point is (1, 1) and top-right point is (2, 2)).
# 
# 
# 
# Example 1:
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4],
# ⁠ [1,3,2,4],
# ⁠ [2,3,3,4]
# ]
# 
# Return true. All 5 rectangles together form an exact cover of a rectangular
# region.
# 
# 
# 
# 
# 
# 
# Example 2:
# 
# rectangles = [
# ⁠ [1,1,2,3],
# ⁠ [1,3,2,4],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4]
# ]
# 
# Return false. Because there is a gap between the two rectangular
# regions.
# 
# 
# 
# 
# 
# 
# Example 3:
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [3,2,4,4]
# ]
# 
# Return false. Because there is a gap in the top center.
# 
# 
# 
# 
# 
# 
# Example 4:
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [2,2,4,4]
# ]
# 
# Return false. Because two of the rectangles overlap with each other.
# 
# 
# 
# 
#
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        x1 = y1 = float('inf')
        x2 = y2 = float('-inf')
        corners = set()
        area = 0
        for rec in rectangles:
            x1 = min(x1, rec[0])
            y1 = min(y1, rec[1])
            x2 = max(x2, rec[2])
            y2 = max(y2, rec[3])

            area += (rec[2]-rec[0])*(rec[3]-rec[1])

            # get 4 corners
            c1 = (rec[0], rec[1])
            c2 = (rec[0], rec[3])
            c3 = (rec[2], rec[1])
            c4 = (rec[2], rec[3])
            c = [c1, c2, c3, c4]

            for corner in c:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

        if len(corners) != 4:   return False
        finalCorners = [(x1,y1), (x1,y2), (x2,y1), (x2,y2)]
        for f in finalCorners:
            if f not in corners:
                return False
        return area == (x2-x1)*(y2-y1)
        
