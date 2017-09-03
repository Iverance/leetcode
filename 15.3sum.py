#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum
#
# Medium (21.58%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array S of n integers, are there elements a, b, c in S such that a +
# b + c = 0? Find all unique triplets in the array which gives the sum of
# zero.
# 
# Note: The solution set must not contain duplicate triplets.
# 
# 
# For example, given array S = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if i and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if num + nums[left] + nums[right] == 0:
                    result.append([num, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif num + nums[left] + nums[right] < 0:
                    left += 1
                elif num + nums[left] + nums[right] > 0:
                    right -= 1
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]])

