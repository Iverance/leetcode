#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray
#
# Easy (39.65%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
# 
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# 
# click to show more practice.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        maxSum = dp[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] if dp[i-1]+nums[i] < 0 else dp[i-1]+nums[i]
            maxSum = max(maxSum, dp[i])
        return maxSum
