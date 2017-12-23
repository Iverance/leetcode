#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray
#
# Easy (30.22%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.  
# 
# You need to find the shortest such subarray and output its length.
# 
# Example 1:
# 
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# 
# 
# 
# Note:
# 
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=. 
# 
# 
#
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxV, minV = float('-inf'), float('inf')
        left = right = -1
        for i in range(n):
            maxV = max(maxV, nums[i])   # search for the maxvalue L to R
            minV = min(minV, nums[n-1-i])   # search for the minvalue R to L

            if nums[i] < maxV:
                right = i
            if nums[n-1-i] > minV:
                left = n-1-i

        return 0 if left == -1 else right-left+1
def main():
    print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5)
    print(Solution().findUnsortedSubarray([2, 3,4,5,6,7,7]) == 0)
if __name__ == "__main__":
    main()
