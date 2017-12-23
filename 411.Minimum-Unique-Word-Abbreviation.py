"""
A string such as "word" contains the following abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.

Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.

Note:
In the case of multiple answers as shown in the second example below, you may return any one of them.
Assume length of target string = m, and dictionary size = n. You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.
Examples:
"apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

"apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
"""

class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        import collections
        n = len(target)
        # conflict candidate
        c = {sum((target[i]!=c)<<i for i, c in enumerate(word)) for word in dictionary if len(word) == n}
        # print(c)

        if not c:
            return str(n)

        # get the possibel abbv, which contain the different char in all candidates, has more consecutive 0
        bits = max((i for i in range(2**n) if all(d & i for d in c)),
               key=lambda bits: sum((bits >> i) & 3 == 0 for i in range(n-1)))
        # print(bits)

        # turn ans to abbv:
        ans = ''
        count = 0
        for i in range(n):
            if bits & 1:
                if count > 0:
                    ans += str(count)
                    count = 0
                ans += target[i]
            else:
                count += 1
            bits >>= 1
        return ans + str(count) if count > 0 else ans
