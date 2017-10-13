#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive
#
# Hard (25.56%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# 
# Given an unsorted integer array, find the first missing positive integer.
# 
# 
# 
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# 
# 
# 
# Your algorithm should run in O(n) time and uses constant space.
# 
#
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums += 0,
        n = len(nums)
        for i in range(n):
            while 0 <= nums[i] < n and nums[i] != nums[nums[i]]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(n):
            if nums[i] != i:
                return i
        return n
if __name__ == '__main__':
    s = Solution()
    assert s.firstMissingPositive([3,-1,4,2]) == 1
    assert s.firstMissingPositive([1,2,3,4]) == 5
    assert s.firstMissingPositive([3, 4, -1, 1]) == 2
    assert s.firstMissingPositive([1, 2, 0]) == 3
    assert s.firstMissingPositive([]) == 1
