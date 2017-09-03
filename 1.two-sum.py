#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum
#
# Easy (33.72%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[3,2,4]\n6'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# 
# Example:
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]'''
        d = {}
        for idx, val in enumerate(nums):
            if target - val in d:
                return [d[target-val], idx]
            else:
                d[val] = idx

def main():
    Solution().twoSum([2,3,5], 5)
    Solution().twoSum([-3,4,3,90], 0)
    Solution().twoSum([-1,-2,-3,-4,-5], -8)
if __name__ == "__main__":
    main()
