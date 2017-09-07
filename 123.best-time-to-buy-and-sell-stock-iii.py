#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii
#
# Hard (29.34%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1 = hold2 = float('-inf')
        sold1 = sold2 = 0
        for price in prices:
            sold2 = max(sold2, hold2+price)
            hold2 = max(hold2, sold1-price)
            sold1 = max(sold1, hold1+price)
            hold1 = max(hold1, -price)

        return sold2
        
