"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        preSum = collections.defaultdict(int)
        preSum[0] = 1
        curSum = 0
        res = 0
        for i in range(n):
            curSum += nums[i]
            if curSum - k in preSum:
                res += preSum[curSum - k]
            preSum[curSum] += 1
        return res

