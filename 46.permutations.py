#
# [46] Permutations
#
# https://leetcode.com/problems/permutations
#
# Medium (43.66%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3]'
#
# 
# Given a collection of distinct numbers, return all possible permutations.
# 
# 
# 
# For example,
# [1,2,3] have the following permutations:
# 
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        # 1 in length of nums, means all presnt and selectable
        mask = (1 << n) - 1
        def dfs(arr, remainMask):
            if not remainMask:
                res.append(arr)
                return
            for idx, val in enumerate(nums):
                # check if selectable. e.g. mask 101 means num[1] is selected
                if remainMask & (1 << idx):
                    dfs(arr + [val], remainMask^(1 << idx))
        dfs([],mask)
        return res
if __name__ == "__main__":
    sol = Solution()
        
