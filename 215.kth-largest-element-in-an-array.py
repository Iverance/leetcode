#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array
#
# Medium (39.31%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]\n1'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return
        
        def partition(arr):
            lo, hi = 0, len(arr)-1
            mi = 0
            pivot = arr[0]
            while mi <= hi:
                if arr[mi] < pivot:
                    arr[mi], arr[hi] = arr[hi], arr[mi]
                    hi -= 1
                elif arr[mi] > pivot:
                    arr[lo], arr[mi] = arr[mi], arr[lo]
                    lo += 1
                    mi += 1
                else:    mi += 1
            return lo
        
        n = len(nums)
        pos = partition(nums)
        # print(nums, k, pos)
        if pos+1 > k:
            return self.findKthLargest(nums[:pos], k)
        elif pos+1 < k:
            return self.findKthLargest(nums[pos+1:], k-pos-1)
        else:
            return nums[pos]
        """
        O(nlgn)
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)
        """
