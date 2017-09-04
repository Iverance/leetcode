#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game
#
# Medium (29.51%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,3,1,1,4]'
#
# 
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# 
# Each element in the array represents your maximum jump length at that
# position. 
# 
# 
# Determine if you are able to reach the last index.
# 
# 
# 
# For example:
# A = [2,3,1,1,4], return true.
# 
# 
# A = [3,2,1,0,4], return false.
# 
#
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        n = len(nums)
        memo = 0            # current longest reachable point
        for i in range(len(nums)):
            if i > memo:    # at this point i is not reachable further
                return False
            step = nums[i]
            memo = max(memo, i + step)
        return True
if __name__ == "__main__":
    sol = Solution()
    assert sol.canJump([0]) == True
    assert sol.canJump([0,2,3]) == False
    assert sol.canJump([1,2,3]) ==True
