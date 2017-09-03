#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree
#
# Hard (29.81%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0,1]'
#
# 
# Two elements of a binary search tree (BST) are swapped by mistake.
# 
# Recover the tree without changing its structure.
# 
# 
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a
# constant space solution?
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.node1, self.node2 = None, None
        self.prev = TreeNode(sys.maxint * -1)
        self.inorder(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val

    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)

        #print(node.val, self.prev.val)
        if not self.node1 and self.prev.val >= node.val:
            #print('node1',self.prev.val)
            self.node1 = self.prev
        if self.node1 and self.prev.val >= node.val:
            #print('node2',self.prev.val)
            self.node2 = node
        self.prev = node

        self.inorder(node.right)
        
