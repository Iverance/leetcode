#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii
#
# Medium (33.04%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,1,2]'
#
# 
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# 
# 
# For example,
# [1,1,2] have the following unique permutations:
# 
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        remains = sorted(nums)
        def dfs(arr, remain):
            if not remain:
                res.append(arr)
                return
            for idx, val in enumerate(remain):
                if idx > 0 and remain[idx] == remain[idx-1]:
                    continue
                dfs(arr+[val], remain[:idx]+remain[idx+1:])
        dfs([], remains)
        return res
