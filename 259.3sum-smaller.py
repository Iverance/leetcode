#
# [259] 3Sum Smaller
#
# https://leetcode.com/problems/3sum-smaller
#
# algorithms
# Medium (41.76%)
# Total Accepted:    31.4K
# Total Submissions: 75.2K
# Testcase Example:  '[]\n0'
#
# Given an array of n integers nums and a target, find the number of index
# triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] +
# nums[j] + nums[k] < target.
# 
# For example, given nums = [-2, 0, 1, 3], and target = 2.
# 
# Return 2. Because there are two triplets which sums are less than 2:
# 
# [-2, 0, 1]
# [-2, 0, 3]
# 
# 
# Follow up:
# Could you solve it in O(n2) runtime?
# 
#
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] < target:
                    res += k-j
                    j+=1
                else:
                    k-=1
        return res
        
