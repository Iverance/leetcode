#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three
#
# Easy (40.32%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '27'
#
# 
# ⁠   Given an integer, write a function to determine if it is a power of
# three.
# 
# 
# ⁠   Follow up:
# ⁠   Could you do it without using any loop / recursion?
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n>0) and 3**19%n==0
        
