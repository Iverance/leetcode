#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii
#
# Easy (32.34%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n0'
#
# 
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
#
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or not k:
            return False

        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                if i - d[nums[i]] <= k:
                    return True
                else:
                    d[nums[i]] = i
        return False
        
