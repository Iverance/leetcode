#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii
#
# Medium (34.06%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Note: This is an extension of House Robber.
# 
# After robbing those houses on that street, the thief has found himself a new
# place for his thievery so that he will not get too much attention. This time,
# all houses at this place are arranged in a circle. That means the first house
# is the neighbor of the last one. Meanwhile, the security system for these
# houses remain the same as for those in the previous street. 
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        robFirst = 0
        one, two = 0, 0
        for i in range(len(nums)-1):
            house = nums[i]
            robFirst = max(two + house, one)
            two = one
            one = robFirst

        notRobFirst = 0
        one, two = 0, 0
        for i in range(1,len(nums)):
            house = nums[i]
            notRobFirst = max(two + house, one)
            two = one
            one = notRobFirst
        return max(robFirst,notRobFirst)
        
