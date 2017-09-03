#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence
#
# Medium (28.46%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1\n1'
#
# The set [1,2,3,…,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 
# Given n and k, return the kth permutation sequence.
# 
# Note: Given n will be between 1 and 9 inclusive.
#
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = []
        nums = []
        f = 1
        for i in range(1,n+1):
            f *= i
            nums.append(str(i))
            factorial.append(f)
        k -= 1
        ans = ""
        for digit in range(1, n+1):
            q, r = divmod(k, factorial[n-digit-1])
            ans += nums[q]
            del nums[q]
            k = r
        return ans
        
