#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors
#
# Medium (38.09%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0]'
#
# 
# Given an array with n objects colored red, white or blue, sort them so that
# objects of the same color are adjacent, with the colors in the order red,
# white and blue.
# 
# 
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# 
# 
# Note:
# You are not suppose to use the library's sort function for this problem.
# 
# 
# click to show follow up.
# 
# 
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with an one-pass algorithm using only constant space?
# 
# 
#
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, k = 0, n - 1
        j = 0
        while j <= k:
            if nums[j] < 1:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            elif nums[j] > 1:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1
        
