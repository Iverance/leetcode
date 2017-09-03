#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii
#
# Medium (33.41%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 
# Given a collection of candidate numbers (C) and a target number (T), find all
# unique combinations in C where the candidate numbers sums to T.
# 
# 
# Each number in C may only be used once in the combination.
# 
# Note:
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# 
# 
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
# 
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
#
class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if i > idx and options[i] == options[i-1]:
                continue
            val = target - options[i]
            self.backtrack(options, val, ans, cmbn + [options[i]], i+1)
        
