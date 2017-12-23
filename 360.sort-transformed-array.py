#
# [360] Sort Transformed Array
#
# https://leetcode.com/problems/sort-transformed-array
#
# algorithms
# Medium (44.56%)
# Total Accepted:    14.2K
# Total Submissions: 31.9K
# Testcase Example:  '[-4,-2,2,4]\n1\n3\n5'
#
# 
# Given a sorted array of integers nums and integer values a, b and c.  Apply a
# quadratic function of the form f(x) = ax2 + bx + c to each element x in the
# array. 
# 
# The returned array must be in sorted order.
# 
# Expected time complexity: O(n)
# 
# Example:
# 
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
# 
# Result: [3, 9, 15, 33]
# 
# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
# 
# Result: [-23, -5, 1, 7]
# 
# 
# 
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def f(x):
            return a*x**2+b*x+c

        l, r = 0, len(nums)-1
        res = []
        while l <= r:
            if a > 0:
                if f(nums[l]) >= f(nums[r]):
                    res.append(f(nums[l]))
                    l+=1
                else:
                    res.append(f(nums[r]))
                    r-=1
            if a <= 0:
                if f(nums[l]) >= f(nums[r]):
                    res.append(f(nums[r]))
                    r-=1
                else:
                    res.append(f(nums[l]))
                    l+=1
        return res if a <= 0 else res[::-1]
        
