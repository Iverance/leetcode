#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii
#
# Hard (23.25%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. You may assume the dictionary does not contain
# duplicate words.
# 
# 
# 
# Return all such possible sentences.
# 
# 
# 
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
# 
# 
# 
# A solution is ["cats and dog", "cat sand dog"].
# 
# 
# 
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a
# set of strings). Please reload the code definition to get the latest changes.
# 
#
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not wordDict or not s:
            return []
        
        def dfs(i, memo):
            if i not in memo:
                memo[i] = []
                for word in wordDict:
                    j = i+len(word)
                    if s[i:j] == word:
                        dfs(j, memo)
                        for tail in memo[j]:
                            if tail == '':
                                memo[i].append(s[i:j])
                            else:
                                memo[i].append(s[i:j] + " " + tail)            
        n = len(s)
        memo = {n:['']}
        dfs(0, memo)
        return memo[0]
if __name__ == "__main__":
    sol = Solution()
    assert sol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]) == ["cat sand dog","cats and dog"]
        
