#
# [288] Unique Word Abbreviation
#
# https://leetcode.com/problems/unique-word-abbreviation
#
# algorithms
# Medium (17.35%)
# Total Accepted:    29.6K
# Total Submissions: 170.8K
# Testcase Example:  '["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]\n[[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]'
#
# An abbreviation of a word follows the form <first letter><number><last
# letter>. Below are some examples of word abbreviations:
# 
# a) it                      --> it    (no abbreviation)
# 
# ⁠    1
# b) d|o|g                   --> d1g
# 
# ⁠             1    1  1
# ⁠    1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n
# 
# ⁠             1
# ⁠    1---5----0
# d) l|ocalizatio|n          --> l10n
# 
# 
# Assume you have a dictionary and given a word, find whether its abbreviation
# is unique in the dictionary. A word's abbreviation is unique if no other word
# from the dictionary has the same abbreviation.
# 
# Example: 
# 
# Given dictionary = [ "deer", "door", "cake", "card" ]
# 
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true
# 
# 
#
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        import collections
        self.d = collections.defaultdict(set)
        for w in dictionary:
            if len(w) > 2:
                self.d[w[0]+str(len(w)-2)+w[-1]].add(w)        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 2:
            return True
        key = word[0]+str(len(word)-2)+word[-1]
        if key not in self.d:
            return True
        else:
            if word in self.d[key] and len(self.d[key]) == 1:
                return True
        return False
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
