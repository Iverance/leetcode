#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman
#
# Medium (44.47%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
# Given an integer, convert it to a roman numeral.
# 
# 
# Input is guaranteed to be within the range from 1 to 3999.
#
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        numerals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanStr = ''
        while num != 0:
            for roman, numeral in zip(romans, numerals):
                if num >= numeral:
                    romanStr += roman
                    num -= numeral
                    break
        return romanStr
if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(3999) == "MMMCMXCIX")
    print(sol.intToRoman(444) == "CDXLIV")
            

        
