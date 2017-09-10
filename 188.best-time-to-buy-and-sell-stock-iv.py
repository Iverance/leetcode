#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv
#
# Hard (24.30%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '2\n[]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most k
# transactions.
# 
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        if k >= n//2:
            return self.quickSolve(prices)

        dp = [[0] * n for _ in range(k+1)]
        for i in range(1, k + 1):
            hold = -prices[0]   # 假設第一天有買
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1],          #今天之前已經賣出的最大利潤(結束第i次交易)
                               hold + prices[j])    #今天賣出的最大利潤
                hold = max(hold,                    #今天之前已經買進後剩餘的錢(開始第i次交易)
                           dp[i-1][j-1] - prices[j])#今天之才買進後剩餘的錢(開始第i次交易)
        return dp[-1][-1]
    
    def quickSolve(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        return profit
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(2, [1, 5, 3, 6, 1, 7]))
    print(sol.maxProfit(2, [7, 1, 5, 3, 6, 4]))
    print(sol.maxProfit(2, [7, 6, 4, 3, 1]))
        
