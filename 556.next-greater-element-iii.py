#
# [556] Next Greater Element III
#
# https://leetcode.com/problems/next-greater-element-iii
#
# Medium (28.86%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '12'
#
# 
# Given a positive 32-bit integer n, you need to find the smallest 32-bit
# integer which has exactly the same digits existing in the integer n and is
# greater in value than n. If no such positive 32-bit integer exists, you need
# to return -1.
# 
# Example 1:
# 
# Input: 12
# Output: 21
# 
# 
# 
# Example 2:
# 
# Input: 21
# Output: -1
# 
# 
#
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = list(str(n))
        n = len(num)
        j = n - 1
        # j is 5 in 18354321
        while j > 0 and num[j-1] >= num[j]:
            j -= 1

        if j > 0:
            i = n - 1
            # i is 4 in 18354321
            while i >= j and num[j-1] >= num[i]:
                i -= 1
            # swap 3 and 4 in 18354321
            num[i], num[j-1] = num[j-1], num[i]
        else:
            return -1

        num[j:] = num[j:][::-1]
        ans = int("".join(num))
        return  -1 if ans > 2**31-1 else ans
        
