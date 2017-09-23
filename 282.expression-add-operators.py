#
# [282] Expression Add Operators
#
# https://leetcode.com/problems/expression-add-operators
#
# Hard (29.80%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"123"\n6'
#
# 
# Given a string that contains only digits 0-9 and a target value, return all
# possibilities to add binary operators (not unary) +, -, or * between the
# digits so they evaluate to the target value.
# 
# 
# Examples: 
# "123", 6 -> ["1+2+3", "1*2*3"] 
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []
# 
# 
# Credits:Special thanks to @davidtan1890 for adding this problem and creating
# all test cases.
#
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        l = []
        n = len(num)
        def backtrack(result, formula, idx, multi):
            if idx == n:
                if result == target:
                    l.append(formula)
                return
            for i in range(idx+1, n+1):
                number = int(num[idx:i])
                tail = num[idx:i]
                if num[idx] == '0'  and i-idx>1:
                    break
                if idx == 0:
                    backtrack(number, tail, i, number)
                else:
                    backtrack(result-number, formula+"-"+tail, i, -number)
                    backtrack(result+number, formula+"+"+tail, i, number)
                    backtrack(result-multi+(multi*number), formula+"*"+tail, i, multi*number)
        backtrack(0,'',0,0)
        return l
if __name__ == "__main__":
    sol = Solution()
    print(sol.addOperators("123",6))
    print(sol.addOperators("232",8))
    print(sol.addOperators("1005",5))
    print(sol.addOperators("1000005",5))
