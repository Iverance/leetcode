#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes
#
# Easy (26.61%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Description:
# Count the number of prime numbers less than a non-negative number, n.
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        d = [True for _ in range(n)]
        d[0] = False
        d[1] = False
        for i in range(2, int(math.sqrt(n))+1):
            if d[i]:
                x = i**2
                while x < n:
                    d[x] = False
                    x += i
        return d.count(True)
if __name__ == "__main__":
    s = Solution()
    assert s.countPrimes(1) == 0
    assert s.countPrimes(0) == 0
    assert s.countPrimes(2) == 0
    assert s.countPrimes(3) == 1
    assert s.countPrimes(10) == 4
    assert s.countPrimes(120) == 30
