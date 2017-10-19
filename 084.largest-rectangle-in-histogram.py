#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram
#
# Hard (26.84%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.
# 
#
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack, maxA = [], 0
        heights.append(0)
        for idx, val in enumerate(heights):
            while stack and heights[stack[-1]] > val:
                idxH = stack.pop()
                h = heights[idxH]
                maxA = max(maxA, h*(idx-stack[-1]-1 if stack else idx))    
            stack.append(idx)
        return maxA
        """
        ***TLE Solution***
        if not heights:
            return 0
        minV, ptr = heights[0], 0
        for idx, val in enumerate(heights):
            if val <= minV:
                minV = val
                ptr = idx
        maxArea = minV * len(heights)
        left = self.largestRectangleArea(heights[:ptr])
        right = self.largestRectangleArea(heights[ptr+1:])
        return max(maxArea,left,right)
        """
if __name__ == "__main__":
    s = Solution()
    assert s.largestRectangleArea([1,9,3]) == 9
    assert s.largestRectangleArea([1]) == 1
    assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
    assert s.largestRectangleArea([4,2,0,3,2,4,3,4]) == 10
    assert s.largestRectangleArea([5,4,3,2,1]) == 9
