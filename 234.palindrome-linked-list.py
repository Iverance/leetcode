#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list
#
# Easy (32.79%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow = fast = head
        # find the mid and reverse first half
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:    # second half is one digit smaller when odd
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
        
