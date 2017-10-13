#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals
#
# Medium (30.04%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# 
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
# 
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        result = [Interval(-1*sys.maxint, -1*sys.maxint)]
        intervals.sort(key = lambda interval:interval.start)
        for interval in intervals:
            if result[-1].end < interval.start:
                result += interval,
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result[1:]

