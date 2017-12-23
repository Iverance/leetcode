#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons
#
# algorithms
# Hard (43.17%)
# Total Accepted:    32.4K
# Total Submissions: 74.8K
# Testcase Example:  '[3,1,5,8]'
#
# 
# ⁠   Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
# ⁠   number on it represented by array nums.
# 
# ⁠   You are asked to burst all the balloons. If the you burst
# ⁠   balloon i you will get nums[left] * nums[i] * nums[right] coins. Here
# left
# ⁠   and right are adjacent indices of i. After the burst, the left and right
# ⁠   then becomes adjacent.
# 
# 
# ⁠   Find the maximum coins you can collect by bursting the balloons wisely.
# 
# 
# ⁠   Note: 
# ⁠   (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore
# you can not burst them.
# ⁠   (2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 
# 
# 
# 
# ⁠   Example:
# 
# 
# ⁠   Given [3, 1, 5, 8]
# 
# 
# ⁠   Return 167
# 
# 
# ⁠   nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
# ⁠  coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP: get the last burst case first, then increasing the length until n
        nums = [1] + [x for x in nums if x > 0] + [1]
        n = len(nums)
        memo = [[0]*n for _ in range(n)]

        for length in range(2, n):
            for left in range(n-length):
                right = left + length
                for i in range(left+1, right):
                    memo[left][right] = max(memo[left][right], nums[left]*nums[i]*nums[right] + memo[left][i] + memo[i][right])
        return memo[0][n-1]
        """
        # D&C: same idea but top down with memorization
        def burst(left, right, memo):
            if left == right - 1:
                return 0
            if memo[left][right]:
                return memo[left][right]
            ans = 0
            for i in range(left+1, right):
                ans = max(ans, nums[left]*nums[i]*nums[right] + burst(i, right, memo) + burst(left, i, memo))
            memo[left][right] = ans
            return ans

        return burst(0, n-1, memo)
        """
        
