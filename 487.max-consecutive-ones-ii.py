#
# [487] Max Consecutive Ones II
#
# https://leetcode.com/problems/max-consecutive-ones-ii
#
# algorithms
# Medium (45.74%)
# Total Accepted:    9.4K
# Total Submissions: 20.5K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# 
# Given a binary array, find the maximum number of consecutive 1s in this array
# if you can flip at most one 0.
# 
# 
# Example 1:
# 
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of
# consecutive 1s.
# ⁠   After flipping, the maximum number of consecutive 1s is 4.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
# 
# Follow up:
# What if the input numbers come in one by one as an infinite stream? In other
# words, you can't store all numbers coming from the stream as it's too large
# to hold in memory. Could you solve it efficiently?
# 
#
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k, n = 1, len(nums)
        left = 0
        zero = res = 0
        for right in range(n):
            num = nums[right]
            if num == 0:
                zero += 1
            while left < right and zero > k:
                if nums[left] == 0:
                    zero -= 1
                left+=1
            # print(nums[left:right+1])
            res = max(res,right-left+1)
        return res        
