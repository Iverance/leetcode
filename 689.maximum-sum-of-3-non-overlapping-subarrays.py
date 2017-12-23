#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays
#
# algorithms
# Hard (41.10%)
# Total Accepted:    5.9K
# Total Submissions: 14.4K
# Testcase Example:  '[1,2,1,2,6,7,5,1]\n2'
#
# 
# In a given array nums of positive integers, find three non-overlapping
# subarrays with maximum sum.
# 
# 
# Each subarray will be of size k, and we want to maximize the sum of all 3*k
# entries.
# 
# 
# Return the result as a list of indices representing the starting position of
# each interval (0-indexed).  If there are multiple answers, return the
# lexicographically smallest one.
# 
# Example:
# 
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting
# indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be
# lexicographically larger.
# 
# 
# 
# Note:
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).
# 
#
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        sums = nums
        right = [[0,0]]*n   #right[i]: max subarray start in interval 0~i
        left = [[0,0]]*n    #left[i]: max subarray start in interval 0~i
        for i in range(1,n):  sums[i] = sums[i-1] + nums[i]

        #cal all possible subarray in the left (starting from left)
        val = sums[k-1]
        for i in range(n-2*k):
            if i < k:
                left[i] = [0, val]
            elif sums[i]-sums[i-k] > val:
                val = sums[i]-sums[i-k]
                left[i] = [i-k+1, val]
            else:
                left[i] = left[i-1]
        # print(left)

        #cal all possible subarray in the right (starting from right)
        val = sums[n-1]-sums[n-1-k]
        for i in range(n-1, 2*k-1, -1):
            if i >= n-k:
                right[i] = [n-k, val]
            elif sums[i+k-1]-sums[i-1] >= val:
                val = sums[i+k-1]-sums[i-1]
                right[i] = [i, val]
            else:
                right[i] = right[i+1]
        # print(right)

        # cal all the mid interval and get the max left and right
        res, val = [], 0
        for i in range(k, n-k):
            m = sums[i+k-1] - sums[i-1]
            l, r = left[i-1][1], right[i+k][1]
            if l+m+r > val:
                val = l+m+r
                res = [left[i-1][0], i, right[i+k][0]]
        return res
        
