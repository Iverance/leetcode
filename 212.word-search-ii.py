#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii
#
# Hard (23.54%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["oaan","etae","ihkr","iflv"]\n["oath","pea","eat","rain"]'
#
# 
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
# 
# 
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
# 
# 
# 
# For example,
# Given words = ["oath","pea","eat","rain"] and board = 
# 
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# 
# 
# Return ["eat","oath"].
# 
# 
# 
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# 
# 
# click to show hint.
# 
# You would need to optimize your backtracking to pass the larger test. Could
# you stop backtracking earlier?
# 
# If the current candidate does not exist in all words' prefix, you could stop
# backtracking immediately. What kind of data structure could answer such query
# efficiently? Does a hash table work? Why or why not? How about a Trie? If you
# would like to learn how to implement a basic trie, please work on this
# problem: Implement Trie (Prefix Tree) first.
# 
#
class TrieNode:
    def __init__(self):
        self.childs = dict()
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            if ch not in node.childs:
                node.childs[ch] = TrieNode()
            node = node.childs[ch]
        node.isWord = True
'''    def remove(self, word):
        """
        Unflag a word in the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            if ch in node.childs:
                node = node.childs[ch]
        node.isWord = False
'''     
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not words or not board:
            return []
        trie = Trie()
        result = []
        m = len(board)
        n = len(board[0])
        for w in words:
            trie.insert(w)
        for i in range(m):
            board[i] = list(board[i])

        def dfs(i, j, node, w):
            #print(i,j,w)
            c = board[i][j]
            if c == '#' or c not in node.childs:
                return
            nextNode = node.childs[c]
            w += c
            if nextNode.isWord:
                result.append(w)
                nextNode.isWord = False
            board[i][j] = '#'
            if i < m-1: dfs(i+1, j, nextNode,w)
            if i > 0: dfs(i-1, j, nextNode,w)
            if j < n-1: dfs(i, j+1, nextNode,w)
            if j > 0: dfs(i, j-1, nextNode,w)
            board[i][j] = c

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root, '')
        return result
if __name__ == "__main__":
    s = Solution()
    print(s.findWords(["a"],["a"]))
    print(s.findWords(["oaan","etae","ihkr","iflv"],["oath","pea","eat","rain"]))
    print(s.findWords(["aa"],["aaa"]))
    print(s.findWords(["abc","aed","afg"],["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]))
