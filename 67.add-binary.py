#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary
#
# Easy (32.66%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"0"\n"0"'
#
# 
# Given two binary strings, return their sum (also a binary string).
# 
# 
# 
# For example,
# a = "11"
# b = "1"
# Return "100".
# 
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if int(a) == 0:
            return b
        if int(b) == 0:
            return a
        res = []
        A = list(a)
        B = list(b)
        offset = 0
        while A or B or offset > 0:
            d1 = int(A.pop()) if A else 0
            d2 = int(B.pop()) if B else 0
            add = d1+d2+offset
            offset = add // 2
            res.append(str(add%2))
        return "".join(reversed(res))
    #or return bin(int(a,2)+int(b,2))[2:]

        
