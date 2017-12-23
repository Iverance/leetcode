#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
#
# algorithms
# Medium (41.31%)
# Total Accepted:    50.8K
# Total Submissions: 122.8K
# Testcase Example:  '[1,2,3,0,2]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like
# (ie, buy one and sell one share of the stock multiple times) with the
# following restrictions:
# 
# 
# ⁠   You may not engage in multiple transactions at the same time (ie, you
# must sell the stock before you buy again).
# ⁠   After you sell your stock, you cannot buy stock on next day. (ie,
# cooldown 1 day)
# 
# 
# Example:
# 
# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        sell = [0 for _ in range(n)]
        buy = [0 for _ in range(n)]
        rest = [0 for _ in range(n)]
        # init
        sell[0] = float('-inf')
        buy[0] = -prices[0]
        rest[0] = 0

        for i in range(1, len(prices)):
            price = prices[i]
            # buy then sell
            sell[i] = buy[i-1]+price
            # not buy vs cooldown then buy
            buy[i] = max(buy[i-1], rest[i-1]-price)
            # sell then rest vs rest then rest
            rest[i] = max(sell[i-1], rest[i-1])

        # checking rest and sell since ending move with buy always reduce money
        return max(rest[-1], sell[-1])
        
