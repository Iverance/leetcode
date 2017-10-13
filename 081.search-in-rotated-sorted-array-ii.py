#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii
#
# Medium (32.78%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n5'
#
# 
# Follow up for "Search in Rotated Sorted Array":
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
# Write a function to determine if a given target is in the array.
# 
# The array may contain duplicates.
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == nums[r] == target:
                return True
            while nums[l] == nums[r] and l <= r:
                r -= 1
            mid = l + ((r-l)//2)
            if target == nums[mid]:
                return True
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return False
        
