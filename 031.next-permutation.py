#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation
#
# Medium (28.77%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]'
#
# 
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # find start of decreasing sequence
        j = n-1
        while j > 0 and nums[j-1] >= nums[j]:
            j -= 1

        if j > 0:
            i = n-1
            # find the next greater number of j-1 in the decreasing sequence
            while j <= i and nums[j-1] >= nums[i]:
                i -= 1
            nums[j-1], nums[i] = nums[i], nums[j-1]

        #reverse decreasing sequence
        nums[j:] = nums[j:][::-1]
