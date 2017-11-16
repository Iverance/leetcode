#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path
#
# algorithms
# Easy (33.03%)
# Total Accepted:    8.3K
# Total Submissions: 25.1K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
# 
# Note: The length of path between two nodes is represented by the number of
# edges between them.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# 
# 
# Output:
# 
# 2
# 
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input:
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# 
# 
# Output:
# 
# 2
# 
# 
# 
# Note:
# The given binary tree has not more than 10000 nodes.  The height of the tree
# is not more than 1000.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
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
        luv_left, luv_right = self.dfs(node.left), self.dfs(node.right)
        left = luv_left+1 if node.left and node.val == node.left.val else 0
        right = luv_right+1 if node.right and node.val == node.right.val else 0
        self.res = max(self.res,left+right)
        return max(right,left)
        
