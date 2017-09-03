#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal
#
# Medium (17.46%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1\n5'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
# 
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
# 
# For example,
# 
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# 
# 
# 
# Credits:Special thanks to @Shangrila for adding this problem and creating all
# test cases.
#
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        sign = (numerator ^ denominator) < 0
        numerator, denominator = abs(numerator), abs(denominator)
        r, q = numerator%denominator, numerator//denominator
        ans = ('', '-')[sign] + str(q)
        
        if r == 0:
            return ans
        else:
            ans = [ans,'.']

        idx = len(ans)
        remainder = {r:idx}
        while True:
            r *= 10
            q = r//denominator
            r = r % denominator
            ans.append(str(q))
            if r in remainder:
                ans.insert(remainder[r], '(')
                ans.append(')')
                return "".join(ans)
            if r == 0:
                return "".join(ans)
            idx += 1
            remainder[r] = idx

if __name__ == "__main__":
    sol = Solution()
    assert sol.fractionToDecimal(1,5) == "0.2"
    assert sol.fractionToDecimal(1,6) == "0.1(6)"
    assert sol.fractionToDecimal(1,3) == "0.(3)"
    assert sol.fractionToDecimal(0,-5) == "0"
