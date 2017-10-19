#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water
#
# Hard (36.81%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# 
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after
# raining. 
# 
# 
# 
# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# 
# 
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
#
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n = len(height)
        ans = 0
        left, right = 0, n-1
        Lwall, Rwall = height[left], height[right]
        while left < right:
            if height[left]>height[right]:
                ans += (Rwall - height[right])
                right -= 1
                Rwall = max(Rwall, height[right])
            else:
                ans += (Lwall - height[left])
                left += 1
                Lwall = max(Lwall, height[left])
        return ans

if __name__ == "__main__":
    s = Solution()
    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert s.trap([4,2,3]) == 1


