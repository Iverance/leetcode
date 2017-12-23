#
# [298] Binary Tree Longest Consecutive Sequence
#
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence
#
# algorithms
# Medium (41.36%)
# Total Accepted:    36.6K
# Total Submissions: 88.6K
# Testcase Example:  '[1,null,3,2,4,null,null,null,5]'
#
# 
# Given a binary tree, find the length of the longest consecutive sequence
# path.
# 
# 
# The path refers to any sequence of nodes from some starting node to any node
# in the tree along the parent-child connections. The longest consecutive path
# need to be from parent to child (cannot be the reverse).
# 
# 
# 
# For example,
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   / \
# ⁠  2   4
# ⁠       \
# ⁠        5
# 
# Longest consecutive sequence path is 3-4-5, so return 3. 
# 
# ⁠  2
# ⁠   \
# ⁠    3
# ⁠   / 
# ⁠  2    
# ⁠ / 
# ⁠1
# 
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            right = dfs(node.right)

            left = left + 1 if node.left and node.val+1 == node.left.val else 1
            right = right + 1 if node.right and node.val+1 == node.right.val else 1
            self.res = max(self.res, left, right)
            return max(left,right)
        dfs(root)
        return self.res
        
