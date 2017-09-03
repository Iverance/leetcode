#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray
#
# Medium (25.37%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[-2]'
#
#
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
#
#
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
#
#


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        min_n, max_n = 1, 1
        ans = float('-inf')
        for num in nums:
            min_n *= num
            max_n *= num
            min_n, max_n = min(min_n, max_n, num), max(min_n, max_n, num)
            ans = max(ans, max_n)
            
        return ans
if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProduct([2,3,-2,4]) == 6
    assert sol.maxProduct([1,0]) == 1
    assert sol.maxProduct([3,-1,4]) == 4
