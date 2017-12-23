#
# [247] Strobogrammatic Number II
#
# https://leetcode.com/problems/strobogrammatic-number-ii
#
# algorithms
# Medium (40.50%)
# Total Accepted:    24.4K
# Total Submissions: 60.3K
# Testcase Example:  '2'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# Find all strobogrammatic numbers that are of length = n. 
# For example,
# Given n = 2, return ["11","69","88","96"].
# 
#
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        self.n = n
        self.res = []
        self.map = {"6":"9", "8":"8", "9":"6", "1":"1", "0":"0"}
        if n & 1:
            for ch in '108':
                self.recur(1,ch)
        else:
            self.recur(0,'')
#        print(self.res)
        return self.res
    def recur(self, size, s):
        if size == self.n and s[0] != '0' or self.n == 1:
            self.res.append(s)
            return
        elif size > self.n:
            return
        for ch in self.map:
           self.recur(size+2, ch + s + self.map[ch])
if __name__ == "__main__":
    s = Solution()
    assert s.findStrobogrammatic(1)
    assert s.findStrobogrammatic(2)
    assert s.findStrobogrammatic(3)

