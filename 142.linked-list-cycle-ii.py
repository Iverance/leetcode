#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii
#
# Medium (30.98%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\nno cycle'
#
# 
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
# 
# 
# 
# Note: Do not modify the linked list.
# 
# 
# Follow up:
# Can you solve it without using extra space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Floyd ring detection
        slow = fast = head
        while fast and fast.next:
            slow = slow.next        #1 step
            fast = fast.next.next   #2 step
            if slow == fast:
                break
        else:
            return None

        slow = head
        while slow != fast:
            slow = slow.next    #1 step
            fast = fast.next    #1 step
        return slow
        
