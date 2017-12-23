#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs
#
# algorithms
# Hard (26.59%)
# Total Accepted:    31.7K
# Total Submissions: 119.1K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# 
# ⁠   Given a list of unique words, find all pairs of distinct indices (i, j)
# in the given list, so that the concatenation of the two words, i.e. words[i]
# + words[j] is a palindrome.
# 
# 
# 
# ⁠   Example 1:
# ⁠   Given words = ["bat", "tab", "cat"]
# ⁠   Return [[0, 1], [1, 0]]
# ⁠   The palindromes are ["battab", "tabbat"]
# 
# 
# ⁠   Example 2:
# ⁠   Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# ⁠   Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# ⁠   The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.index = -1
        # save the index that 
        self.arr = []
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        self.res = []
        self.palindrome = set()
        root = TrieNode()
        for i in range(len(words)):
            w = words[i]
            self.buildTree(root, w, i)
        for i in range(len(words)):
            self.search(root, words[i], i)
        return self.res
            
    def search(self, root, word, idx):
        for i in range(len(word)):
            ch = word[i]
            if root.index != -1 and root.index != idx and self.isPalindrome(word[i:]):
                self.res.append([idx,root.index])
            if ch not in root.nodes:
                return
            root = root.nodes[ch]
        # if there's more word match and having same suffix
        for i in root.arr:
            if i == idx:
                continue
            self.res.append([idx, i])
            
    def buildTree(self, root, word, idx):
        n = len(word)
        for i in range(n-1,-1,-1):
            c = word[i]
            if c not in root.nodes:
                root.nodes[c] = TrieNode()
            if self.isPalindrome(word[:i+1]):
                root.arr.append(idx)
            root = root.nodes[c]
        root.index = idx
        root.arr.append(idx)
    
    def isPalindrome(self, word):
        if word in self.palindrome:
            return True
        s,e = 0, len(word)-1
        while s < e:
            if word[s] != word[e]:  return False
            s+=1
            e-=1
        self.palindrome.add(word)
        return True
