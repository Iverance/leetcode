#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list
#
# Medium (35.25%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# 
# Given a binary tree, flatten it to a linked list in-place.
# 
# 
# 
# For example,
# Given
# 
# ⁠        1
# ⁠       / \
# ⁠      2   5
# ⁠     / \   \
# ⁠    3   4   6
# 
# 
# 
# The flattened tree should look like:
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠     \
# ⁠      3
# ⁠       \
# ⁠        4
# ⁠         \
# ⁠          5
# ⁠           \
# ⁠            6
# 
# 
# click to show hints.
# 
# Hints:
# If you notice carefully in the flattened tree, each node's right child points
# to the next node of a pre-order traversal.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.preorder = []
        def dfs(node):
            if not node:
                return
            self.preorder.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        pre = root
        for node in self.preorder[1:]:
            pre.left = None
            pre.right = node
            pre = node
        
