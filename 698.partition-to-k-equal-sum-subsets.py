#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets
#
# algorithms
# Medium (37.17%)
# Total Accepted:    7.4K
# Total Submissions: 19.9K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into k non-empty subsets whose sums are all
# equal.
# 
# Example 1:
# 
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
# 
# 
# 
# Note:
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.
# 
#
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = sum(nums)
        memo = {}
        if k == 1: return True
        if k<=0 or s % k != 0 or k > len(nums):
            return False
        nums.sort(reverse=True) # Speed up the iteration by finding the best candidate
        def dfs(visited, cur_sum, tar_sum, k):
            # print(visited, cur_sum, tar_sum, k)
            h = str(visited)
            if h in memo:
                return memo[h]
            if cur_sum == tar_sum:
                return dfs(visited, 0, tar_sum, k-1)
            if k == 0:
                return True
            for i in range(len(nums)):
                if not visited[i] and cur_sum+nums[i] <= tar_sum:
                    visited[i] = True
                    if dfs(visited, cur_sum+nums[i], tar_sum, k):
                        memo[h] = True
                        return memo[h]
                    visited[i] = False
            memo[h] = False
            return memo[h]

        return dfs([False]*len(nums), 0, s/k, k)

if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartitionKSubsets([3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269],5))
