#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words
#
# Hard (22.14%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '123'
#
# 
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 231 - 1.
# 
# 
# For example,
# 
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
#
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        belowTwenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousnads = ["", "Thousand", "Million", "Billion"]
        def parse(n):
            s = ''
            if n == 0:
                return s
            lastTwo = n % 100
            firstOne = n // 100
            if lastTwo < 20:
                s += belowTwenty[lastTwo]
            else:
                s += " ".join([tens[lastTwo//10],belowTwenty[lastTwo%10]])
            if firstOne:
                s = " ".join([belowTwenty[firstOne], "Hundred", s])
            return s.strip()


        if num == 0:
            return 'Zero'
        res = ''
        cnt = 0
        while num > 0:
            if num % 1000 > 0:
                res = " ".join([parse(num % 1000), thousnads[cnt], res])
            cnt += 1
            num //= 1000
        return res.strip()
