#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate
#
# Easy (45.70%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# 
# Given an array of integers, find if the array contains any duplicates. Your
# function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
# 
#
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                return True

        return False
        
