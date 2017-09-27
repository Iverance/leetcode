#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists
#
# Hard (27.39%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# 
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return

        l = []
        dummy = ListNode(0)
        curr = dummy
        for node in lists:
            if node:
                heapq.heappush(l, (node.val, node))

        while l:
            _, node = heapq.heappop(l)
            if node.next:
                heapq.heappush(l, (node.next.val, node.next))
            curr.next = node
            curr = node

        return dummy.next
        
