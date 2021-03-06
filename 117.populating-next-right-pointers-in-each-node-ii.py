#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
#
# Medium (33.77%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '{}'
#
# Follow up for problem "Populating Next Right Pointers in Each Node".
# What if the given tree could be any binary tree? Would your previous solution
# still work?
# 
# Note:
# You may only use constant extra space.
# 
# 
# For example,
# Given the following binary tree,
# 
# ⁠        1
# ⁠      /  \
# ⁠     2    3
# ⁠    / \    \
# ⁠   4   5    7
# 
# 
# 
# After calling your function, the tree should look like:
# 
# ⁠        1 -> NULL
# ⁠      /  \
# ⁠     2 -> 3 -> NULL
# ⁠    / \    \
# ⁠   4-> 5 -> 7 -> NULL
# 
# 
#
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        q = [root]
        while q:
            isFirst = True
            levelSize = len(q)
            pre = None
            for _ in range(levelSize):
                node = q.pop(0)
                if node.left:   q.append(node.left)
                if node.right:  q.append(node.right)
                if isFirst:
                    isFirst = False
                    pre = node
                    continue
                pre.next = node
                pre = node
