#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree
#
# algorithms
# Easy (44.55%)
# Total Accepted:    37.2K
# Total Submissions: 83.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# 
# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
# 
# 
# 
# Example:
# Given a binary tree 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Note:
# The length of path between two nodes is represented by the number of edges
# between them.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if root:
            self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return
        left, right = self.dfs(node.left), self.dfs(node.right)
        left = left+1 if node.left else 0
        right = right+1 if node.right else 0
        self.res = max(self.res,left+right)
        return max(right,left)
