#
# [449] Serialize and Deserialize BST
#
# https://leetcode.com/problems/serialize-and-deserialize-bst
#
# Medium (42.38%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,1,3]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment. 
# 
# Design an algorithm to serialize and deserialize a binary search tree. There
# is no restriction on how your serialization/deserialization algorithm should
# work. You just need to ensure that a binary search tree can be serialized to
# a string and this string can be deserialized to the original tree
# structure.
# 
# 
# The encoded string should be as compact as possible.
# 
# 
# 
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        q = [root]
        coded = [root.val]
        while q:
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                if not node:    continue
                q.append(node.left)
                q.append(node.right)
            coded+=[node.val if node else 'N' for node in q]
        #print(coded)
        return coded
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == 'N':
            return
        d = list(data)
        root = TreeNode(d.pop(0))
        q = [root]
        while q:
            node = q.pop(0)
            
            l = d.pop(0)
            if l != 'N':
                node.left = TreeNode(l)
                q.append(node.left)
                
            r = d.pop(0)
            if r != 'N':
                node.right = TreeNode(r)
                q.append(node.right)
            
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
