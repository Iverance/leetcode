#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number
#
# Medium (22.74%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Key(str):
    def __lt__(a, b):
        return a + b < b + a
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return '0'
        nums = sorted([str(num) for num in nums],key=Key, reverse=True)
        return ''.join(nums).lstrip("0") or "0"
