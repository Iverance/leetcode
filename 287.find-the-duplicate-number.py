#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number
#
# Medium (43.34%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,1]'
#
# 
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# 
# 
# Note:
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # length n+1, and element val won't exceed n
        # We can imagine every val is pointing to some inedx
        # If there is duplicated one, there must a cycle
        # implement Floyd Cycle detection
        # Floyd ring detection
        if not nums or len(nums) == 1:
            return 0
        slow = fast = 0
        while slow == 0 or  slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
if __name__ == "__main__":
    sol = Solution()
    assert sol.findDuplicate([1,3,4,2,2]) == 2
