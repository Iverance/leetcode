#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer
#
# Medium (26.24%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '{}'
#
# 
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# 
# 
# Return a deep copy of the list.
# 
#
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        table = {} # {oriNode: cloneNode}
        def getNode(node, existNodes):
            if node in existNodes:
                return existNodes[node]
            else:
                newNode = RandomListNode(node.label)
                table[node] = newNode
                return newNode


        dummy = RandomListNode(0)
        ptr_clone = dummy
        ptr = head
        while ptr:
            newNode = getNode(ptr, table)
            if ptr.random:
                newNode.random = getNode(ptr.random, table)
            ptr_clone.next = newNode
            ptr, ptr_clone = ptr.next, ptr_clone.next
        return dummy.next
