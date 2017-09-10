#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list
#
# Medium (28.81%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # divide the list by getting mid node
        slow = fast = head
        prev = slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # cut the list
        prev.next = None
        
        node1 = self.sortList(head)
        node2 = self.sortList(slow)
        
        return self.merge(node1, node2)
        
    def merge(self, l1, l2):
        dummy = curr = ListNode(None)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr, l1 = curr.next, l1.next
            else:
                curr.next = l2
                curr, l2 = curr.next, l2.next
        
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        return dummy.next
