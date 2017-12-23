#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements
#
# algorithms
# Medium (35.17%)
# Total Accepted:    10.7K
# Total Submissions: 30.4K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# 
# Given a sorted array, two integers k and x, find the k closest elements to x
# in the array.  The result should also be sorted in ascending order.
# If there is a tie,  the smaller elements are always preferred.
# 
# 
# Example 1:
# 
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# 
# 
# 
# 
# Example 2:
# 
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# 
# 
# 
# Note:
# 
# The value k is positive and will always be smaller than the length of the
# sorted array.
# ⁠Length of the given array is positive and will not exceed 104
# ⁠Absolute value of elements in the array and x will not exceed 104
# 
# 
# 
# 
# 
# 
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list
# of integers). Please reload the code definition to get the latest changes.
# 
#
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if k >= len(arr):
            return arr
        n = len(arr)
        # i = j = self.binarySearch(arr,x)
        i = j = bisect.bisect_left(arr, x)
        while j-i<k:
            if i == 0:  return arr[:k]
            elif j == n:    return arr[-k:]
            elif x-arr[i-1] <= arr[j]-x:  i-=1
            else:   j+=1
        return arr[i:j]
        
    def binarySearch(self, arr, x):
        n = len(arr)
        left, right = 0, n - 1
        while left <= right:            
            mid = (left + right)//2
            if arr[mid] > x:
                right = mid - 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                return mid
        return left        
