#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one
#
# Easy (38.75%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0]'
#
# Given a non-negative integer represented as a non-empty array of digits, plus
# one to the integer.
# 
# You may assume the integer do not contain any leading zero, except the number
# 0 itself.
# 
# The digits are stored such that the most significant digit is at the head of
# the list.
#
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return
        n = len(digits)
        for i in range(n-1, -1, -1):
            if i == n-1 or carry:
                digits[i] += 1
                carry = digits[i]//10
                digits[i] %= 10
            if not carry:
                break
        if carry:
            digits = [1]+digits
        return digits
