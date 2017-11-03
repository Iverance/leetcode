#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings
#
# Medium (55.31%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"abc"'
#
# 
# Given a string, your task is to count how many palindromic substrings in this
# string.
# 
# 
# 
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters. 
# 
# 
# Example 1:
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# 
# Example 2:
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# Note:
# 
# The input string length won't exceed 1000.
# 
# 
#
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.count = 0
        for i in range(len(s)):
            self.check(s,i,i)  # odd case
            self.check(s,i,i+1)# even case
        return self.count
    def check(self,s ,left, right):
        n = len(s)
        while left >= 0  and right < n:
            if s[right] != s[left]:
                break
            self.count+=1
            right += 1
            left -= 1
if __name__ == "__main__":
    s = Solution()
    assert s.countSubstrings("abc") ==  3
    assert(s.countSubstrings("aaa") == 6)
