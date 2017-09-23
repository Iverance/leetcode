#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator
#
# Hard (27.17%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"0"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
# 
# You may assume that the given expression is always valid.
# 
# Some examples:
# 
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
# 
# 
# 
# 
# Note: Do not use the eval built-in library function.
# 
#
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        operand = 1
        num = 0
        result = 0
        for ch in s:
            if ch in '0123456789':
                num = num*10 + int(ch)
            elif ch == '+':
                result += operand*num
                num = 0
                operand = 1
            elif ch == '-':
                result += operand*num
                num = 0
                operand = -1
            elif ch == '(':
                stack.append(result)
                stack.append(operand)
                result = 0
                operand = 1
            elif ch == ')':
                result += operand*num
                num = 0
                operand = stack.pop()
                prevResult = stack.pop()
                result = prevResult + operand*result
            else:
                continue
            #print(operand,num,result,stack)

        if num != 0:
            result += operand*num
        return result
if __name__ == "__main__":
    sol = Solution()
    assert sol.calculate("1 + 1") == 2
    assert sol.calculate(" 2-1 + 2 ") == 3
    assert sol.calculate("(1+(4+5+2)-3)+(6+8)") == 23
