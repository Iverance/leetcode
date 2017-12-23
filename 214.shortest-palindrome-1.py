#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome
#
# algorithms
# Hard (24.68%)
# Total Accepted:    46.2K
# Total Submissions: 187K
# Testcase Example:  '"aacecaaa"'
#
# 
# Given a string S, you are allowed to convert it to a palindrome by adding
# characters in front of it. Find and return the shortest palindrome you can
# find by performing this transformation.
# 
# 
# For example: 
# Given "aacecaaa", return "aaacecaaa".
# Given "abcd", return "dcbabcd".
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases. Thanks to @Freezen for additional test cases.
#
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        maxj, c = 1, 0
        while c <= len(s)/2:
            i = j = c
            while j+1 < len(s) and s[j+1] == s[j]:
                j += 1
            if i > len(s)-j-1:
                break
            c = j+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            if i < 0:
                maxj = max(maxj, j)
            print(s[maxj:], c)
        return s[maxj:][::-1]+s
        #gxybakbkabbfmbnnnjjjyxqg
