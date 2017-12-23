#
# [413] Arithmetic Slices
#
# https://leetcode.com/problems/arithmetic-slices
#
# algorithms
# Medium (54.58%)
# Total Accepted:    31.6K
# Total Submissions: 57.9K
# Testcase Example:  '[1,2,3,4]'
#
# A sequence of number is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the
# same.
# 
# For example, these are arithmetic sequence:
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# 
# The following sequence is not arithmetic. 1, 1, 2, 5, 7 
# 
# 
# A zero-indexed array A consisting of N numbers is given. A slice of that
# array is any pair of integers (P, Q) such that 0 <= P < Q < N.
# 
# A slice (P, Q) of array A is called arithmetic if the sequence:
# ⁠   A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this
# means that P + 1 < Q.
# 
# The function should return the number of arithmetic slices in the array A. 
# 
# 
# Example:
# 
# A = [1, 2, 3, 4]
# 
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3,
# 4] itself.
# 
#
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<3:
            return 0
        # dp[i] means the sequence ending at A[i]
        dp = [0 for _ in range(len(A))]
        dp[2] = 1 if (A[0]-A[1]) == (A[1]-A[2]) else 0
        res = dp[2]
        for i in range(3, len(A)):
            if (A[i-2]-A[i-1]) == (A[i-1]-A[i]):
                dp[i] = dp[i-1] + 1
            # if length increses, we cover different permutations by adding up dp[i]
            # [1,2,3,4] has [1,2,3] in length 3 (dp[3]) and [2,3,4], [1,2,3,4] (dp[2])
            res += dp[i]
        return res
