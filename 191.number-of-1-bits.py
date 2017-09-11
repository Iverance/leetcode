#
# [191] Number of 1 Bits
#
# https://leetcode.com/problems/number-of-1-bits
#
# Easy (39.67%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '           0 (00000000000000000000000000000000)'
#
# Write a function that takes an unsigned integer and returns the number of ’1'
# bits it has (also known as the Hamming weight).
# 
# For example, the 32-bit integer ’11' has binary representation
# 00000000000000000000000000001011, so the function should return 3.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            if 0 < n & 3 < 3:
                cnt += 1
            elif n & 3 == 3:
                cnt += 2
            n >>= 2
        return cnt
if __name__ == "__main__":
    sol = Solution()
    assert sol.hammingWeight(11) == 3
