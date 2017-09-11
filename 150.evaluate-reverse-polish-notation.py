#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation
#
# Medium (27.28%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["18"]'
#
# 
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# 
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# 
# 
# Some examples:
# 
# ⁠ ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
# ⁠ ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
# 
# 
#
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        park = []
        for ch in tokens:
            if ch not in '+-*/':
                park.append(int(ch))
            else:
                sec = park.pop()
                first = park.pop()
                if ch == '+':
                    park.append(first + sec)
                elif ch == '-':
                    park.append(first - sec)
                elif ch == '*':
                    park.append(first * sec)
                elif first ^ sec >= 0:
                    park.append(first // sec)
                else:   # Note: In Python3, -1 // 2 == -1
                    park.append(-(abs(first) // abs(sec)))
        return park.pop()
        
