#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum
#
# Hard (26.23%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3]'
#
# 
# Given a binary tree, find the maximum path sum.
# 
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# 
# For example:
# Given the below binary tree,
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 
# 
# Return 6.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float('-inf')
        self.traverse(root)
        return self.maxSum
        
    def traverse(self, node):
        if not node:
            return 0
        right = max(0, self.traverse(node.right))
        left = max(0, self.traverse(node.left))
        self.maxSum = max(self.maxSum, node.val + right + left)
        return max(right, left) + node.val        
