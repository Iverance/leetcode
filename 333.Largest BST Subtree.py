"""
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:
    10
    / \
   5  15
  / \   \
 1   8   7
The Largest BST Subtree in this case is the highlighted one.
The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""

class Solution:
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        return: maxV, minV, nodeCnt
        """
        self.maxV = 0
        def dfs(node):
            if not node:
                return float('-inf'), float('inf'), 0
            max1, min1, c1 = dfs(node.left)
            max2, min2, c2 = dfs(node.right)
            BSTCnt = -1
            if max1 < node.val < min2 and c1 != -1 and c2 != -1:
                BSTCnt = c1 + c2 + 1
            #print(node.val,max(node.val, max2, max1), min(node.val, min1, min2), BSTCnt)
            self.maxV = max(self.maxV, BSTCnt)
            return max(node.val, max2, max1), min(node.val, min1, min2), BSTCnt
        dfs(root)
        return self.maxV
