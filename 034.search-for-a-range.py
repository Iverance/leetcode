#
# [34] Search for a Range
#
# https://leetcode.com/problems/search-for-a-range
#
# Medium (31.37%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers sorted in ascending order, find the starting and
# ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# 
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
# 
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        left, right = 0, n-1
        res = [-1,-1]
        # find left one
        while left < right:
            print(left,right)
            mid = (right+left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return res
        res[0] = left
        right = n-1
        while left < right:
            mid = right - (right-left)//2
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid
        res[1] = right
        return res
if __name__ == "__main__":
    sol = Solution()
    assert sol.searchRange([5,7,7,8,8,10], 8) == [3,4]
        
