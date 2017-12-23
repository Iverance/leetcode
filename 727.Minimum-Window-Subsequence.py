"""
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:
Input:
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
"""
import collections
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        pre = collections.defaultdict(list)
        for i, c in enumerate(T, -1):
            pre[c].append(i)
        for val in pre.values():
            val.reverse()
        # print(pre)

        start_index = [None] * (len(T) + 1)
        lo, hi = float('-inf'), 0
        for i, c in enumerate(S):
            # print(start_index)
            start_index[-1] = i
            for p in pre[c]:
                if start_index[p] is not None:
                    start_index[p + 1] = start_index[p]
            if (c == T[-1] and start_index[-2] is not None
                and i - start_index[-2] < hi - lo):
                lo, hi = start_index[-2], i
        if lo < 0:
            return ''
        else:
            return S[lo:hi+1]

# if __name__ == "__main__":
#     s = Solution()
#     assert s.minWindow("cnhczmccqouqadqtmjjzl","dq") == "dq"
#     assert s.minWindow("abcdebdde","bde") == "bcde"
#     assert s.minWindow("fgrqsqsnodwmxzkzxwqegkndaa","kzed") == "kzxwqegknd"
#     assert s.minWindow("fgrqsqsnodwmxzkzxwqegkndaa","fnok") == "fgrqsqsnodwmxzk"
#     assert s.minWindow("cnhczmccqouqadqtmjjzl","mm") == "mccqouqadqtm"

