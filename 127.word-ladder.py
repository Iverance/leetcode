#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder
#
# Medium (19.46%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
# 
# 
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# 
# For example,
# 
# 
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# 
# 
# 
# Note:
# 
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# 
# 
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a
# set of strings). Please reload the code definition to get the latest changes.
# 
#
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        candid = set(wordList)
        q = [beginWord]
        dist = 1
        while q:
            level = len(q)
            for _ in range(level):
                w = q.pop(0)
                if w == endWord:
                    return dist
                # add its neighbor
                remove = []
                for i in range(len(w)):
                    for alph in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = w[:i] + alph + w[i+1:]
                        if nextWord in candid:
                            q.append(nextWord)
                            candid.remove(nextWord)
            dist += 1
        return 0
if __name__ == "__main__":
    s = Solution()
    assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
