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
        if not s:
            return ''
        n = len(s)
        end = 0
        for start in range(n-1, -1, -1):
            if s[start] == s[end]:
                end += 1
        suffix = s[end:]
        return s if end == n else suffix[::-1] + self.shortestPalindrome(s[:end]) + suffix

#         self.palindromeCache = set()
#         prefix = ''
#         for i in range(n, -1, -1):
#             if self.isPalindrome(s[:i]):
#                 prefix = s[i:][::-1]
#                 break
#         return prefix+s

#     def isPalindrome(self, word):
#         if word in self.palindromeCache:
#             return True
#         l, r = 0, len(word)-1
#         while l<r:
#             if word[l]!=word[r]:    return False
#             l+=1
#             r-=1
#         self.palindromeCache.add(word)
#         return True
        
