#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
#
# Medium (39.79%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
#
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return min(nums)
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            if abs(r-l) == 1:
                return min(nums[r], nums[l])
            mid = int((l + r) / 2)
            if nums[mid] < nums[r]:
                r = mid
            if nums[mid] > nums[r]:
                l =  mid



if __name__ == "__main__":
    sol = Solution()
    arr = [7, 0, 1, 2, 3, 4, 5, 6]
    print(sol.findMin(arr))
    arr = [6, 7, 0, 1, 2, 3, 4, 5]
    print(sol.findMin(arr))
    arr = [5, 6, 7, 0, 1, 2, 3, 4]
    print(sol.findMin(arr))
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    print(sol.findMin(arr))
    arr = [3, 4, 5, 6, 7, 0, 1, 2]
    print(sol.findMin(arr))
    arr = [2, 3, 4, 5, 6, 7, 0, 1]
    print(sol.findMin(arr))
    arr = [1, 2, 3, 4, 5, 6, 7, 0]
    print(sol.findMin(arr))
    arr = [0, 1, 2, 3, 4, 5, 6, 7]
    print(sol.findMin(arr))        
