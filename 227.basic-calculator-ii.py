#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii
#
# Medium (29.30%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"0"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
# 
# You may assume that the given expression is always valid.
# 
# Some examples:
# 
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# 
# 
# 
# 
# Note: Do not use the eval built-in library function.
# 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        multi = 0
        num = 0
        res = 0
        operand = '+'
        for i in range(n):
            if s[i] in '+-/*':
                if operand == '+':
                    multi = num
                    res += num
                elif operand == '-':
                    multi = -num
                    res -= num
                elif operand == '*':
                    res -= multi
                    multi = multi*num
                    res += multi
                elif operand == '/':
                    res -= multi
                    multi = multi//num if multi^num >= 0 else -(abs(multi)//abs(num))
                    res += multi
                num = 0
                operand = s[i]
            elif s[i] in '0123456789':
                num *= 10
                num += int(s[i])
#            print(operand, multi, num, res)

        if num != 0:
            if operand == '+':
                multi = num
                res += num
            elif operand == '-':
                multi = -num
                res -= num
            elif operand == '*':
                res -= multi
                multi = multi*num
                res += multi
            elif operand == '/':
                res -= multi
                multi = multi//num if multi^num >= 0 else -(abs(multi)//abs(num))
                res += multi

        return res   
if __name__ == "__main__":
    s = Solution()
    assert s.calculate("14-3/2") == 13
    assert s.calculate("3+2*2") == 7
    assert s.calculate("0") == 0
    assert s.calculate(" 3/2 ") == 1
    assert s.calculate(" 3+5 / 2 ")==5
