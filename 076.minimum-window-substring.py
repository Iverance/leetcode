#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring
#
# Hard (25.57%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"a"\n"a"'
#
# 
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# 
# 
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# 
# 
# Minimum window is "BANC".
# 
# 
# 
# Note:
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# 
# 
# If there are multiple such windows, you are guaranteed that there will always
# be only one unique minimum window in S.
# 
#
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        n, cnt = len(s), len(t)
        q = []
        table = {}
        for ch in t:
            table[ch] = table.get(ch, 0) + 1
        p1 = begin = end = 0
        for p2, ch in enumerate(s, 1):
            if ch in table:
                table[ch] -= 1
                if table[ch] >= 0:
                    cnt -= 1
            if cnt == 0:
                # print(s[p1:p2])
                # print(table)
                while True:
                    if s[p1] in table:
                        if table[s[p1]] == 0:
                            break
                        else:
                            table[s[p1]] += 1
                    p1 += 1
                # print(s[p1:p2])
                if not end or p2-p1 < end-begin:
                    begin, end = p1, p2
                table[s[p1]] = 1
                p1 += 1
                cnt = 1
        return s[begin:end]
if __name__ == "__main__":
    s = Solution()
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("AA", "AA") == "AA"
    assert s.minWindow("", "") == ""
    assert s.minWindow("A", "") == ""
