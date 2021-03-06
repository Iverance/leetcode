#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group
#
# Hard (30.87%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n1'
#
# 
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# 
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# You may not alter the values in the nodes, only nodes itself may be changed.
# 
# Only constant memory is allowed.
# 
# 
# For example,
# Given this linked list: 1->2->3->4->5
# 
# 
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# 
# 
# For k = 3, you should return: 3->2->1->4->5
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        notGroupHead,cnt = head,k
        while notGroupHead and cnt > 0:
            notGroupHead = notGroupHead.next
            cnt-=1
        if cnt == 0:
            cnt = k
            prev = None
            tail = head
            while head and cnt > 0:
                tmp = head
                head = head.next
                tmp.next = prev
                prev = tmp
                cnt-=1
            tail.next = self.reverseKGroup(notGroupHead, k)
            return prev
        else:
            return head
