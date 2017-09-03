#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters
#
# Medium (24.20%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        ans, start = 0, 0
        for idx, val in enumerate(s):
            if val in d and d[val] >= start:
                start = d[val]+1
            d[val] = idx
            ans = max(idx - start + 1, ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb") == 3)
    print(sol.lengthOfLongestSubstring("bbbbb") == 1)
    print(sol.lengthOfLongestSubstring("pwwkew") == 3)
    print(sol.lengthOfLongestSubstring("abba") == 2)
    print(sol.lengthOfLongestSubstring("au") == 2)

