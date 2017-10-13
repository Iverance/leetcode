#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum
#
# Medium (26.63%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array S of n integers, are there elements a, b, c, and d in S such
# that a + b + c + d = target? Find all unique quadruplets in the array which
# gives the sum of target.
# 
# Note: The solution set must not contain duplicate quadruplets.
# 
# 
# 
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        for i in range(len(nums)-3):
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    #print(i,j,left,right)
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif total < target:
                        left += 1
                    elif total > target:
                        right -= 1
        return result
if __name__ == "__main__":
    sol = Solution()
    #assert sol.fourSum([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
   # assert sol.fourSum([0,0,0,0], 0) == [[0,0,0,0]]
   # assert sol.fourSum([-1,0,1,2,-1,-4], -1) == [[-4,0,1,2],[-1,-1,0,1]]
