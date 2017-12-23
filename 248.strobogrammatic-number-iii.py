#
# [248] Strobogrammatic Number III
#
# https://leetcode.com/problems/strobogrammatic-number-iii
#
# algorithms
# Hard (32.26%)
# Total Accepted:    10.5K
# Total Submissions: 32.5K
# Testcase Example:  '"0"\n"0"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# Write a function to count the total strobogrammatic numbers that exist in the
# range of low <= num <= high.
# For example,
# Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three
# strobogrammatic numbers.
# 
# 
# Note:
# Because the range might be a large number, the low and high numbers are
# represented as string.
# 
#
class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.low, self.high = low, high
        self.res = 0
        self.map = {"6":"9", "8":"8", "9":"6", "1":"1", "0":"0"}
        for i in range(len(low),len(high)+1):
            self.recur(i, '')
        #print(self.res)
        return self.res
    def recur(self, size, s):
        #print(size,s)
        if size < 0:
            return
        if size == 0:
            if int(self.low) <= int(s) <= int(self.high) and (s[0] != '0' or len(s) == 1):
                self.res += 1
                return
            else:
                return
        if size & 1:
            for ch in '108':
                self.recur(size-1, ch)
        else:
            for ch in self.map:
                self.recur(size-2, ch + s + self.map[ch])
if __name__ == "__main__":
    s = Solution()
    assert s.strobogrammaticInRange("50","100") == 3
    assert s.strobogrammaticInRange("0","0") == 1
        
