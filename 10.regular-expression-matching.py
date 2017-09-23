#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching
#
# Hard (24.14%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"aa"\n"a"'
#
# Implement regular expression matching with support for '.' and '*'.
# 
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
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
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true
# 
#
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sLen, pLen = len(s), len(p)
        dp = [[False for _ in range(pLen+1)] for _ in range(sLen+1)]
        dp[0][0] = True
        for j in range(pLen):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j-1] 
        #for i in range(sLen+1):
        #    dp[i][0] = True 
        for i in range(1, sLen+1):
            for j in range(1, pLen+1):
                pattern = p[j-1]
                char = s[i-1]
                if pattern == '*':
                    repeatChar = p[j-2] 
                    # when current char match the repeat char
                    if char == repeatChar or repeatChar == '.':
                        # one repeatChar, no repeatChar or multiple repeat char
                        dp[i][j] = dp[i][j-1] or dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
                else:
                    dp[i][j] = dp[i-1][j-1] and (pattern == char or pattern == '.')
        return dp[-1][-1]
if __name__ == "__main__":
    s = Solution()
    assert s.isMatch("a", "c*") == False
    assert s.isMatch("aab", "c*a*b") == True
    assert s.isMatch("ab", ".*") ==True
    assert s.isMatch("aaa","aa") == False
    assert s.isMatch("aa", "a*") == True
    assert s.isMatch("aaa","aa") == False

