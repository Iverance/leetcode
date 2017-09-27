#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning
#
# Medium (33.61%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"aab"'
#
# 
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# 
# Return all possible palindrome partitioning of s.
# 
# 
# For example, given s = "aab",
# 
# Return
# 
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        self.DFS(s, [], 0)
        return self.res

    def DFS(self, s, path, idx):
        if idx == len(s):
            self.res += list(path),
            return
        for i in range(idx+1, len(s)+1):
            sub = s[idx:i]
            if self.isPalindrome(sub):
                path += sub,
                self.DFS(s, path, i)
                path.pop()
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))
    print(s.partition("cdd"))
