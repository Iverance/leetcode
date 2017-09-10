#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array
#
# Easy (24.65%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]\n0'
#
# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
# [5,6,7,1,2,3,4]. 
# 
# Note:
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# 
# 
# [show hint]
# Hint:
# Could you do it in-place with O(1) extra space?
# 
# 
# Related problem: Reverse Words in a String II
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution(object):
    
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0,nums.pop())

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        k %= n
        reverse(n-k, n-1)
        reverse(0, n-1-k)
        reverse(0, n-1)
        
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
