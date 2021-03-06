"""
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

"""
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if not n:
            return 0
        if n == 1:
            return k
        diffColor = k*(k-1)
        sameColor = k
        for i in range(2, n):
            tmp = diffColor
            diffColor = (sameColor+diffColor)*(k-1)
            sameColor = tmp
        return sameColor+diffColor
