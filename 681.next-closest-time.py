#
# [681] Next Closest Time
#
# https://leetcode.com/problems/next-closest-time
#
# algorithms
# Medium (43.04%)
# Total Accepted:    8.3K
# Total Submissions: 19.4K
# Testcase Example:  '"19:34"'
#
# Given a time represented in the format "HH:MM", form the next closest time by
# reusing the current digits. There is no limit on how many times a digit can
# be reused.
# 
# You may assume the given input string is always valid. For example, "01:34",
# "12:09" are all valid. "1:34", "12:9" are all invalid.
# 
# Example 1:
# 
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
# which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours
# and 59 minutes later.
# 
# 
# 
# Example 2:
# 
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is
# smaller than the input time numerically.
# 
# 
#
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = list(time.replace(':',''))
        digits = sorted(set(time))
        table = {str(x):i for i, x in enumerate(digits)}

        for i in range(3, -1 , -1):
            ch = time[i]
            if table[ch] != len(digits)-1:
                if i == 3:
                    time[i] = digits[table[ch]+1]
                    break
                if i == 2:
                    if digits[table[ch]+1] > '5':
                        continue
                    time[i] = digits[table[ch]+1]
                    time[i+1] = digits[0]
                    break
                if i == 1:
                    if time[0] == '2' and digits[table[ch]+1] > '3':
                        continue
                    time[i] = digits[table[ch]+1]
                    time[i+1] = time[i+2] = digits[0]
                    break
                else:
                    time = [digits[0] for _ in range(4)]
        return ''.join(time[0:2])+':'+''.join(time[2:])
