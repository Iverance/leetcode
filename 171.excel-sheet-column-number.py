#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number
#
# Easy (47.33%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"A"'
#
# Related to question Excel Sheet Column Title
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        ans = 0
        for ch in s:
            ans *= 26
            ans += ord(ch) - 64
        return ans
        
