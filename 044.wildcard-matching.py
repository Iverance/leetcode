#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching
#
# Hard (20.02%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"aa"\n"a"'
#
# Implement wildcard pattern matching with support for '?' and '*'.
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# 
# The matching should cover the entire input string (not partial).
# 
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
# 
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false
# 
#
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sl, pl = len(s), len(p)
        idx1, idx2 = 0, 0
        lastMatch, starIdx = 0, -1
        while idx1 < sl:
            if idx2 < pl and (p[idx2] == '?' or s[idx1] == p[idx2]):
                idx1 += 1
                idx2 += 1
            elif idx2 < pl and (p[idx2] == '*'):
                starIdx =  idx2
                lastMatch = idx1
                idx2 += 1
            elif starIdx != -1:
                idx2 = starIdx + 1 #back to next pos of last star if 2 chars not matching
                lastMatch += 1
                idx1 = lastMatch
            else: #not matching and no stars
                return False
        while idx2 < pl and p[idx2]=='*':
            idx2 += 1 #going forward if tailing stars
        return idx2 == pl
    
if __name__ == "__main__":
    sol = Solution()
    assert sol.isMatch("aa","a") == False
    assert sol.isMatch("aa","aa") == True
    assert sol.isMatch("aaa","aa") == False
    assert sol.isMatch("aa","*") == True
    assert sol.isMatch("aa","a*") == True
    assert sol.isMatch("ab","?*") == True
    assert sol.isMatch("aab","c*a*b") == False
    assert sol.isMatch("zacabz","*a?b*") == False
    assert sol.isMatch("abefcdgiescdfimde","ab*cd?i*de") == True    
