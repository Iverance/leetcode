#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges
#
# algorithms
# Medium (30.76%)
# Total Accepted:    87.9K
# Total Submissions: 285.9K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# 
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
# 
# Example 1:
# 
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# 
# 
# 
# Example 2:
# 
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# 
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rng = [[float('-inf'),float('-inf')]]
        res = []
        for n in nums:
            if n > rng[-1][-1] + 1:
                rng.append([n])
            elif n == rng[-1][-1] + 1:
                rng[-1].append(n)
        for r in rng[1:]:
            if len(r) == 1:
                res.append(str(r[0]))
            else:
                res.append("->".join([str(r[0]),str(r[-1])]))
        return res
