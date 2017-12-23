"""
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
"""

class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 3
        if n == 0:
            return 0
        # Calculate no A present
        nums = [1, 2, 4]
        for i in xrange(3, n+1):
            nums.append((nums[i-1] + nums[i-2] + nums[i-3])% 1000000007)
        result = nums[n]

        # + A present
        for i in range(1,n+1):
            result += nums[i-1] * nums[n-i] % 1000000007
            result %= 1000000007
        return result

