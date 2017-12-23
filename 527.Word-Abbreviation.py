"""
Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.
"""

import collections, heapq
class TrieNode():
    def __init__(self):
        self.cnt = 0
        self.node = collections.defaultdict(TrieNode)
class Trie():
    def __init__(self):
        self.root = TrieNode()

    def buildTree(self, words):
        # O(nl) n: len(words), l: max(len(words[i]))
        for word in words:
            cur = self.root
            cur.cnt += 1
            for i, ch in enumerate(word):
                cur = cur.node[word[i]]
                cur.cnt += 1


class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        wordSet = collections.defaultdict(list)
        h = []
        ans = ['']*len(dict)
        for i, w in enumerate(dict):
            if len(w) > 3:
                abbv = w[0] + str(len(w)-2) + w[-1]
            else:
                abbv = w
            ans[i] = abbv
            wordSet[abbv] += i,

        for k, v in wordSet.items():
            if len(v) == 1:
                ans[v[0]] = k
            else:
                heapq.heappush(h, (-len(v), k, v)) # make a max heap and solve the collision
        # print(h)
        while h:
            _, _, arr = heapq.heappop(h)
            # del wordSet[k]
            trie = Trie()
            trie.buildTree([dict[i] for i in arr])
            for idx in arr:
                word = dict[idx]
                p = 0 # prefix index
                cur = trie.root
                while cur.cnt > 1:
                    # print(word[p], cur.cnt)
                    cur = cur.node[word[p]]
                    p += 1
                # print(p)
                if len(word) - p + 1 <= 3:
                    ans[idx] = word
                else:
                    ans[idx] = word[:p] + str(len(word)-p-1) + word[-1]
        return ans
