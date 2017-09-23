#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence
#
# Hard (37.01%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# 
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length:
# 4.
# 
# 
# Your algorithm should run in O(n) complexity.
# 
#
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxV = 0
        d = {}
        for num in nums:
            if num not in d:
                r = d.get(num+1, 0)
                l = d.get(num-1, 0)
                leng = r + l + 1
                maxV = max(maxV, leng)
                d[num] = leng
                # update the border
                d[num+r] = leng
                d[num-l] = leng

        return maxV
if __name__ == "__main__":
    sol = Solution()
    assert sol.longestConsecutive([1,2,0,1]) == 3
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2, 5]) == 5
