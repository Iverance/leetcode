#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures
#
# algorithms
# Medium (52.08%)
# Total Accepted:    3.8K
# Total Submissions: 7.4K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 
# Given a list of daily temperatures, produce a list that, for each day in the
# input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
# 
# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73],
# your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# 
# 
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
# 
#
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = []
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            t = temperatures[i]
            while stack and t >= temperatures[stack[-1]]:
                stack.pop()
            res.append(stack[-1] - i if stack else 0)
            stack.append(i)
        return res[::-1]
