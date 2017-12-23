#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters
#
# algorithms
# Hard (29.87%)
# Total Accepted:    34.9K
# Total Submissions: 116.8K
# Testcase Example:  '"bcabc"'
#
# 
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
# 
# 
# 
# Example:
# 
# 
# Given "bcabc"
# Return "abc"
# 
# 
# Given "cbacdcbc"
# Return "acdb"
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        s = list(s)
        n = len(s)
        table = {}
        stack = []
        for ch in s:
            if ch not in table:
                table[ch] = 0
            table[ch] += 1
        for ch in s:
            table[ch] -= 1
            if ch in stack:
                continue
            while stack and ch < stack[-1] and table[stack[-1]] > 0:
                stack.pop()
            stack.append(ch)

        return "".join(stack)

if __name__ == "__main__":
    sol = Solution()
    assert(sol.removeDuplicateLetters("bcabc") == "abc")
    assert(sol.removeDuplicateLetters("cbacdcbc") == "acdb")
    assert(sol.removeDuplicateLetters("ccacbaba") == "acb")
    assert(sol.removeDuplicateLetters("edebbed") == "bed")
    assert(sol.removeDuplicateLetters("abacb") == "abc")

        
