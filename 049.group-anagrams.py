#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams
#
# Medium (34.62%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# 
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:
# 
# [
# ⁠ ["ate", "eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note: All inputs will be in lower-case.
#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        memo = {}
        for s in strs:
            l = "".join(sorted(s))
            if l not in memo:
                memo[l] = []
            memo[l].append(s)
        res = []
        for val in memo.values():
            res.append(val)
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams([]))
       
