"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = set()
        for ch in s:
            if ch in memo:
                memo.remove(ch)
            else:
                memo.add(ch)
        return 0<= len(memo) <= 1

