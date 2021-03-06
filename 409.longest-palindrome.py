#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome
#
# Easy (45.33%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = []
        count = 0
        for ch in s:
            #print(c, ch)
            if ch not in c:
                c.append(ch)
            else:
                c.remove(ch)
                count += 2
        return count + 1 if c else count
        
if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome("abccccdd") == 7
