#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element
#
# Easy (46.82%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        n = len(nums)
        table = {}
        for num in nums:
            table[num] = table.get(num, 0) + 1
            if table[num] > n//2:
                return num
