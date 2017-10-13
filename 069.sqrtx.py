#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx
#
# Easy (27.90%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x.
#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 1
        r = (x+1) >> 1
        while r >= l:
            mid = l + ((r-l)// 2)
            v = mid**2
            if v == x:
                return mid
            elif v > x:
                r = mid - 1
            else:
                l = mid + 1
        return r
if __name__ == "__main__":
    s = Solution()
    assert s.mySqrt(1) == 1
    assert s.mySqrt(2) == 1
    assert s.mySqrt(5) == 2
