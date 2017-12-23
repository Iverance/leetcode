#
# [351] Android Unlock Patterns
#
# https://leetcode.com/problems/android-unlock-patterns
#
# algorithms
# Medium (44.40%)
# Total Accepted:    17.3K
# Total Submissions: 38.9K
# Testcase Example:  '1\n1'
#
# 
# Given an Android 3x3 key lock screen and two integers m and n, where  1 ≤ m ≤
# n ≤ 9, count the total number of unlock patterns of the Android lock screen,
# which consist of minimum of m keys and maximum n keys.
# 
# Rules for a valid pattern:
# 
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any
# other keys, the other keys must have previously selected in the pattern. No
# jumps through non selected key is allowed.
# The order of keys used matters.
# 
# 
# 
# 
# 
# Explanation:
# 
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# 
# 
# 
# Invalid move: 4 - 1 - 3 - 6 
# 
# Line  1 - 3 passes through key 2 which had not been selected in the pattern.
# 
# Invalid move: 4 - 1 - 9 - 2
# 
# Line  1 - 9 passes through key 5 which had not been selected in the pattern.
# 
# Valid move: 2 - 4 - 1 - 3 - 6
# 
# Line 1 - 3 is valid because it passes through key 2, which had been selected
# in the pattern
# 
# Valid move: 6 - 5 - 4 - 1 - 9 - 2
# 
# Line 1 - 9 is valid because it passes through key 5, which had been selected
# in the pattern.
# 
# Example:
# Given m = 1, n = 1, return 9.
# 
# 
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # all the crossing line are invalid, unless they exist in path
        # precalculate it as checking table
        invalid = [[0]*10 for _ in range(10)]
        invalid[1][3] = invalid[3][1] = 2
        invalid[1][7] = invalid[7][1] = 4
        invalid[1][9] = invalid[9][1] = invalid[3][7] = invalid[7][3] = 5
        invalid[2][8] = invalid[8][2] = invalid[4][6] = invalid[6][4] = 5
        invalid[3][9] = invalid[9][3] = 6
        invalid[7][9] = invalid[9][7] = 8
        count = 0
        def dfs(num, path, remain):
            # print(num, path, remain)
            if remain < 0:
                return 0
            elif remain == 0:
                return 1
            else:
                cnt = 0
                path[num] = True
                for i in range(1, 10):
                    if not path[i] and (invalid[num][i] == 0 or path[invalid[num][i]] == True):
                        cnt += dfs(i, path, remain-1)
                path[num] = False
                return cnt
        for i in range(m-1, n):
            count += (dfs(1, [False]*10, i) * 4) #1,3,7,9 are symmetric
            count += (dfs(2, [False]*10, i) * 4) #2,4,6,8 are symmetric
            count += dfs(5, [False]*10, i)
        return count
        
