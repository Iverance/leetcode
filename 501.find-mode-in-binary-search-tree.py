#
# [501] Find Mode in Binary Search Tree
#
# https://leetcode.com/problems/find-mode-in-binary-search-tree
#
# Easy (38.03%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,null,2,2]'
#
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the
# most frequently occurred element) in the given BST.
# 
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
# The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# For example:
# Given BST [1,null,2,2],
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
# 
# 
# 
# return [2].
# 
# 
# Note:
# If a tree has more than one mode, you can return them in any order.
# 
# 
# Follow up:
# Could you do that without using any extra space? (Assume that the implicit
# stack space incurred due to recursion does not count).
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.curVal = self.curCnt = 0
        self.maxCnt = 0
        self.mode = []
        # 第一次先取得頻率最高的個數
        self.inorder(root)
        self.curVal = self.curCnt = 0
        self.mode = [-1]
        # 第二次取得跟頻率最高出現次數的數字
        self.inorder(root)
        
        return self.mode[1:]
    
    def handleVal(self, x):
        if x != self.curVal:
            self.curVal = x
            self.curCnt = 0
        self.curCnt += 1
        if self.curCnt > self.maxCnt:
            self.maxCnt = self.curCnt
        elif self.curCnt == self.maxCnt:
            if self.mode:
                self.mode.append(self.curVal)
                
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.handleVal(node.val)
        self.inorder(node.right)        
