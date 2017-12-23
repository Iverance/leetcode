#
# [616] Add Bold Tag in String
#
# https://leetcode.com/problems/add-bold-tag-in-string
#
# algorithms
# Medium (38.93%)
# Total Accepted:    5.8K
# Total Submissions: 15K
# Testcase Example:  '"abcxyz123"\n["abc","123"]'
#
# Given a string s and a list of strings dict, you need to add a closed pair of
# bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two
# such substrings overlap, you need to wrap them together by only one pair of
# closed bold tag. Also, if two substrings wrapped by bold tags are
# consecutive, you need to combine them. 
# 
# Example 1:
# 
# Input: 
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
# 
# 
# 
# Example 2:
# 
# Input: 
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
# 
# 
# 
# Note:
# 
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000]. 
# 
# 
#
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        # find all the insert points
        intPtr = [[float('-INF')]]
        for i in range(len(s)):
            for w in dict:
                if s[i:i+len(w)] == w:
                    # extend if possible
                    if i <= intPtr[-1][-1] and i+len(w) > intPtr[-1][-1]:
                        intPtr[-1][-1] = i+len(w)
                    # create new only if new interval coming
                    elif i > intPtr[-1][-1] and i+len(w) > intPtr[-1][-1]:
                        intPtr.append([i, i+len(w)])
            # print(intPtr)
        # Split the string and insert the tag
        res, prev = [], 0
        for i, j in intPtr[1:]:
            res.append(s[prev:i]+'<b>'+s[i:j]+'</b>')
            prev = j
        res.append(s[prev:])
        return "".join(res)        
