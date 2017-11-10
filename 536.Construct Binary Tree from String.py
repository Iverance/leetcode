"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        stack = []
        i=0
        while i < len(s):
            #print([x.val for x in stack])
            ch = s[i]
            if ch in '-0123456789':
                j=i+1
                while j<len(s):
                    if s[j] not in '-0123456789':
                        break
                    j+=1
                node = TreeNode(int(s[i:j]))
                if stack:
                    parent = stack[-1]
                    if not parent.left:
                        parent.left = node
                    else:
                        parent.right = node
                stack.append(node)
                i = j
            elif ch == ')':
                stack.pop()
                i+= 1
            else:
                i+=1
        return stack[-1] if stack else None

