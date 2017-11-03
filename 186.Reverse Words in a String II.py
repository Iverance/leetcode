"""
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array

Update (2017-10-16):
We have updated the function signature to accept a character array, so please reset to the default code definition by clicking on the reload button above the code editor. Also, Run Code is now available!
"""
class Solution(object):
    def reverseWords(self, strs):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        if not strs:
            return
        left, right = 0, len(strs)-1
        while left<=right:
            strs[left], strs[right] = strs[right], strs[left]
            left += 1
            right -= 1
        strs.append(' ')
        pre = 0
        for i in range(len(strs)):
            if strs[i] == ' ':
                strs[pre:i] = reversed(strs[pre:i])
                pre = i+1
        strs.pop()

