#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change
#
# Medium (26.62%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]\n0'
#
# 
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# 
# 
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
# 
# 
# 
# Example 2:
# coins = [2], amount = 3
# return -1.
# 
# 
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        dp = [ float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for sub in range(1, amount+1):
            for coin in coins:
                if sub - coin >= 0:
                    dp[sub] = min(dp[sub], dp[sub-coin]+1)
        return (dp[amount], -1)[dp[amount]==float('inf')]
if __name__ == "__main__":
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2],3) == -1

        
