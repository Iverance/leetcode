#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title
#
# Easy (26.19%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases.
#
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n > 0:
            x = (n-1) % 26
            ans = chr(x+65) + ans
            n = (n-1) / 26
        return ans
        
