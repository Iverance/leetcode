#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable
#
# Medium (20.82%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# The update(i, val) function modifies nums by updating the element at index i
# to val.
# 
# Example:
# 
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 
# 
# 
# Note:
# 
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.
# 
# 
#
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.size = len(nums)
        self.arr = nums
        self.bit = [0 for _ in range(self.size+1)]
        for idx, val in enumerate(nums,1):
            self.add(idx,val)
        
    def add(self,i ,val):
        while i <= self.size:
            self.bit[i] += val
            i += self.getLastBit(i)

    def sum(self, i):
        currSum = 0
        while i > 0:
            currSum += self.bit[i]
            i -= self.getLastBit(i)
        return currSum

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.arr[i]
        self.arr[i] = val
        self.add(i+1, diff)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j+1) - self.sum(i)
        
    def getLastBit(self, x):
        return x & -x


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
