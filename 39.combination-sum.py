#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum
#
# Medium (38.22%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,3,6,7]\n7'
#
# 
# Given a set of candidate numbers (C) (without duplicates) and a target number
# (T), find all unique combinations in C where the candidate numbers sums to
# T. 
# 
# 
# The same repeated number may be chosen from C unlimited number of times.
# 
# 
# Note:
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# 
# 
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# 
# [
# ⁠ [7],
# ⁠ [2, 2, 3]
# ]
# 
# 
#
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        ans = []
        self.backtrack(candidates, target, ans, [], 0)
        return ans

    def backtrack(self, options, target, ans, cmbn, idx):
        if target == 0:
            ans+=cmbn,
            return
        elif target < 0:
            return

        for i in range(idx, len(options)):
            val = target - options[i]
            self.backtrack(options, val, ans, cmbn + [options[i]], i)

if __name__ == "__main__":
    sol = Solution()
    candidates = []
    target = 7
    assert sol.combinationSum(candidates, target) == []

    candidates = [2, 3, 6, 7]
    target = 7
    assert sol.combinationSum(candidates, target) == [[2,2,3],[7]]

    candidates = [1]
    target = 1
    assert sol.combinationSum(candidates, target) == [[1]]
