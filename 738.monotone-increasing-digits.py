#
# [738] Monotone Increasing Digits
#
# https://leetcode.com/problems/monotone-increasing-digits
#
# algorithms
# Medium (40.92%)
# Total Accepted:    2.3K
# Total Submissions: 5.7K
# Testcase Example:  '10'
#
# 
# Given a non-negative integer N, find the largest number that is less than or
# equal to N with monotone increasing digits.
# 
# (Recall that an integer has monotone increasing digits if and only if each
# pair of adjacent digits x and y satisfy x <= y.)
# 
# 
# Example 1:
# 
# Input: N = 10
# Output: 9
# 
# 
# 
# Example 2:
# 
# Input: N = 1234
# Output: 1234
# 
# 
# 
# Example 3:
# 
# Input: N = 332
# Output: 299
# 
# 
# 
# Note:
# N is an integer in the range [0, 10^9].
# 
#
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        l = list(str(N))
        i = len(l)-1
        while i > 0 and l[i-1] <= l[i]:
            i -= 1
        if i == 0:
            return N
        else:
            for j in range(i, len(l)):
                l[j] = '9'
            l[i-1] = str(int(l[i-1])-1)
            return self.monotoneIncreasingDigits(int("".join(l)))
        return ans
