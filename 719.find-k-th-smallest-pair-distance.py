#
# [719] Find K-th Smallest Pair Distance
#
# https://leetcode.com/problems/find-k-th-smallest-pair-distance
#
# algorithms
# Hard (25.00%)
# Total Accepted:    2.8K
# Total Submissions: 11.1K
# Testcase Example:  '[1,3,1]\n1'
#
# Given an integer array, return the k-th smallest distance among all the
# pairs. The distance of a pair (A, B) is defined as the absolute difference
# between A and B. 
# 
# Example 1:
# 
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0 
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# 
# 
# 
# Note:
# 
# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.
# 
# 
#
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        [1,1,3,4,5,7,7,9]
        """
        nums.sort()
        lo, hi = 0, nums[-1]-nums[0]
        self.count(nums, 4)
        while lo < hi:
            mid = (hi+lo)/2
            if self.count(nums, mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def count(self, nums, val):
        """
        Count the total number of pair distance which is smaller than val
        """
        count = right = 0
        for left, n in enumerate(nums):
            while right < len(nums)-1 and nums[right+1] - n <= val:
                right += 1
            count += right - left
        return count
