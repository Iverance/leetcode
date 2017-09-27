#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber
#
# Easy (39.03%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases. Also thanks to @ts for adding additional test cases.
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0, 0] for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = nums[i-1] + dp[i-1][0]
        return max(dp[-1][0], dp[-1][1])
        
