#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer
#
# Easy (45.47%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"DCXXI"'
#
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the range from 1 to 3999.
#
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV', 'M', 'D', 'C', 'L', 'X', 'V', 'I']
        numerals = [900, 400, 90, 40, 9, 4, 1000, 500, 100, 50, 10, 5, 1]
        i = ans = 0
        while i < len(s):
            for roman, numeral in zip(romans, numerals):
                if s[i:i+2] == roman:
                    i += 2
                    ans += numeral
                    break
                elif s[i:i+1] == roman:
                    i += 1
                    ans += numeral
                    break
        return ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("MMMCMXCIX") == 3999)
    print(sol.romanToInt("CDXLIV") == 444)



