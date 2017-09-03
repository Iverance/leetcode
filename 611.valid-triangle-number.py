#
# [611] Valid Triangle Number
#
# https://leetcode.com/problems/valid-triangle-number
#
# Medium (38.58%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,2,3,4]'
#
# Given an array consists of non-negative integers,  your task is to count the
# number of triplets chosen from the array that can make triangles if we take
# them as side lengths of a triangle.
# 
# Example 1:
# 
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# 
# 
# 
# Note:
# 
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].
# 
# 
# 
#
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        result = 0
        for i in range(len(nums)-1,1,-1):
            #print(nums[i])
            if nums[i] == 0:
                break
            left = 0
            right = i - 1
            while left < right:
                #print(nums[left],nums[right])
                if nums[i] < nums[left]+nums[right]:
                    result += (right - left)
                    right -= 1
                    continue
                left += 1
        return result
if __name__ == "__main__":
    sol = Solution()
    assert sol.triangleNumber([2,2,3,4])==3
    assert sol.triangleNumber([0,1,1,1])==1
    assert sol.triangleNumber([0,0,0])==0
    assert sol.triangleNumber([1,2,3,4,5,6])==7
                
