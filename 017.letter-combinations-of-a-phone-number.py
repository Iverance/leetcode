#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number
#
# Medium (34.24%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""'
#
# Given a digit string, return all possible letter combinations that the number
# could represent.
# 
# 
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below.
# 
# 
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 
# Note:
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        ans = []

        def dfs(idx, cmbn):
            if idx == len(digits):
                ans.append(cmbn)
                return
            for ch in letters[digits[idx]]:
                dfs(idx + 1, cmbn+ch)

        if digits:        
            dfs(0,"")

        return ans
if __name__ == "__main__":
    sol = Solution()
    assert sol.letterCombinations("") == []
    assert sol.letterCombinations("2") == ["a", "b", "c"]
    assert sol.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
