#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
#
# Hard (37.05%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]'
#
# 
# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# 
# 
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
#
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            if abs(r-l) == 1:
                return min(nums[r], nums[l])
            mid = int((l + r) / 2)
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l =  mid
            else:
                r -= 1
if __name__ == "__main__":
    sol = Solution()
    arr = [0, 1, 1, 1, 1]
    assert sol.findMin(arr) == 0
    arr = [1, 0, 1, 1, 1]
    assert sol.findMin(arr) == 0
    arr = [1, 1, 0, 1, 1]
    assert sol.findMin(arr) == 0
    arr = [1, 1, 1, 0, 1]
    assert sol.findMin(arr) == 0
    arr = [1, 1, 1, 1, 0]
    assert sol.findMin(arr) == 0


