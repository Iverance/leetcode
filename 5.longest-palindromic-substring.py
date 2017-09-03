#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring
#
# Medium (25.13%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example:
# 
# Input: "babad"
# 
# Output: "bab"
# 
# Note: "aba" is also a valid answer.
# 
# 
# 
# Example:
# 
# Input: "cbbd"
# 
# Output: "bb"
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.ans = ""
        self.maxL = 0
        def getLPL(left, right):
            while 0 <= left and right < len(s):
                #print(left, right, s[left], s[right])
                if s[left] != s[right]:
                    break
                if right - left + 1 > self.maxL:
                    self.ans = s[left:right+1]
                    self.maxL = right - left + 1
                right += 1
                left -= 1

        for i in range(len(s)):
            getLPL(i, i)
            getLPL(i,i+1)
            #print(self.ans)

        return self.ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad") == "bab")
    print(sol.longestPalindrome("cbbd") == "bb")
    print(sol.longestPalindrome("") == "")
    print(sol.longestPalindrome("a") == "a")
    print(sol.longestPalindrome("aa") == "aa")
    print(sol.longestPalindrome("baaaab") == "baaaab")
