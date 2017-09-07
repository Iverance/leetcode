#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers
#
# Easy (51.22%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# Example:
# Given a = 1 and b = 2, return 3.
# 
# 
# Credits:Special thanks to @fujiaozhu for adding this problem and creating all
# test cases.
#
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF    # 2**31 - 1 MAX_INT
        MASK = 0xFFFFFFFF   # 2**32 + 1, 32 bits all one's
        while b != 0:
            a, b = (a^b) & MASK, ((a&b) << 1) & MASK
        return a if a <= MAX else ~(a^MASK)
        
