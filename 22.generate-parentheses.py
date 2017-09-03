#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses
#
# Medium (44.57%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(ans, cmbn, left, right):
            if left == right == 0:
                ans.append(cmbn)
                return
            if left > 0:
                dfs(ans, cmbn+'(', left-1, right)
            if right > left and right > 0:
                dfs(ans, cmbn+')', left, right-1)
        ans = []
        dfs(ans, '', n, n)
        return ans
if __name__ == "__main__":
    sol = Solution()
    assert len(sol.generateParenthesis(3)) == 5
