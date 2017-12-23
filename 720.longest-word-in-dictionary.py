#
# [720] Longest Word in Dictionary
#
# https://leetcode.com/problems/longest-word-in-dictionary
#
# algorithms
# Easy (40.46%)
# Total Accepted:    5.4K
# Total Submissions: 13.2K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
# Given a list of strings words representing an English Dictionary, find the
# longest word in words that can be built one character at a time by other
# words in words.  If there is more than one possible answer, return the
# longest word with the smallest lexicographical order.  If there is no answer,
# return the empty string.
# 
# Example 1:
# 
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor",
# and "worl".
# 
# 
# 
# Example 2:
# 
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary.
# However, "apple" is lexicographically smaller than "apply".
# 
# 
# 
# Note:
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].
# 
#
class TrieNode():
    def __init__(self):
        self.isWord = False
        self.child = {}

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]
        node.isWord = True

    def search(self):
        q = [(self.root, '')]
        ans = []
        while q:
            size = len(q)
            for i in range(size):
                node, string = q.pop(0)
                for key in node.child:
                    if node.child[key].isWord:
                        q.append((node.child[key], string+key))
            if q:
                ans = [tup[1] for tup in q]
        ans.sort()
        return ans[0]
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        tree = Trie()
        for word in words:
            tree.insert(word)
        return tree.search()

        
