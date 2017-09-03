#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses
#
# Easy (33.29%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"["'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.
# 
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vals = {
            ")":"(", "}":"{", "]":"[",
        }
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
                continue
            if ch in vals:
               if not stack or vals[ch] != stack.pop():
                    return False

        return (False, True)[len(stack) == 0]
if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()[]{}") == True
    assert sol.isValid("){") == False
    assert sol.isValid("([)]") == False
