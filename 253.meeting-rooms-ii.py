#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii
#
# algorithms
# Medium (39.37%)
# Total Accepted:    55.3K
# Total Submissions: 140.4K
# Testcase Example:  '[]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
# 
# 
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.
# 
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        import heapq
        heap = []
        intervals.sort(key=lambda x:x.start)
        for interval in intervals:
            if not heap or interval.start<heap[0]:
                heapq.heappush(heap, interval.end)
            else:
                heapq.heappushpop(heap, interval.end)
        return len(heap)
        
