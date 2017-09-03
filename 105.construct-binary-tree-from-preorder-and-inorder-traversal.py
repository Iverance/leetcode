#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
#
# Medium (32.18%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n[]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return
        rootVal = preorder.pop(0)
        rootIdx = inorder.index(rootVal)
        node = TreeNode(rootVal)

        node.left = self.buildTree(preorder, inorder[:rootIdx])
        node.right = self.buildTree(preorder, inorder[rootIdx+1:])
        return node
        
