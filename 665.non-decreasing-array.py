#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array
#
# algorithms
# Easy (21.00%)
# Total Accepted:    13.6K
# Total Submissions: 65K
# Testcase Example:  '[4,2,3]'
#
# 
# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
# 
# 
# 
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for
# every i (1 <= i < n).
# 
# 
# Example 1:
# 
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
# 
# 
# 
# Example 2:
# 
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
# 
# 
# 
# Note:
# The n belongs to [1, 10,000].
# 
#
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        [4,2,3]     vs  [4,2,5]
        lower i-1       rising i
        """
        n = len(nums)
        cnt = 0
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                if i-2 < 0 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                elif nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
                cnt+=1
        return cnt <= 1
