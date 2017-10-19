#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes
#
# Easy (50.16%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0,1,0,3,12]'
#
# 
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# 
# 
# For example, given nums  = [0, 1, 0, 3, 12], after calling your function,
# nums should be [1, 3, 12, 0, 0].
# 
# 
# 
# Note:
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        ptr = lastNonZero = 0
        for num in nums:
            if num != 0:
                nums[lastNonZero] = num
                lastNonZero+=1
        while lastNonZero<n:
            nums[lastNonZero] = 0
            lastNonZero+=1
        
