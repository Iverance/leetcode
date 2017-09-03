#
# [165] Compare Version Numbers
#
# https://leetcode.com/problems/compare-version-numbers
#
# Medium (20.03%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"1"\n"0"'
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise
# return 0.
# 
# You may assume that the version strings are non-empty and contain only digits
# and the . character.
# The . character does not represent a decimal point and is used to separate
# number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it
# is the fifth second-level revision of the second first-level revision.
# 
# Here is an example of version numbers ordering:
# 0.1 < 1.1 < 1.2 < 13.37
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ans = 0
        v1 = version1.split('.')
        v2 = version2.split('.')
        while len(v1) != len(v2):
            if len(v1) > len(v2):
                v2 += '0',
            else:
                v1 += '0',
        for i in range(len(v1)):
            subV1, subV2 = v1[i], v2[i]
            while subV1[0] == '0' and int(subV1) != 0: subV1 = subV1[1:]
            while subV2[0] == '0' and int(subV2) != 0: subV2 = subV2[1:]
            intSubV1, intSubV2 = int(subV1), int(subV2)
            if intSubV1 != intSubV2:
                #print(v1,v2)
                return 1 if intSubV1 > intSubV2 else -1
        #print(v1,v2)
        return ans

if __name__ == "__main__":
    sol = Solution()
    assert sol.compareVersion("1.2.1", "1.2") == 1
    assert sol.compareVersion("1.1.5", "1.1.0.2") == 1
    assert sol.compareVersion("0.1", "1.1") == -1
    assert sol.compareVersion("1", "1.0") == 0
    assert sol.compareVersion("1", "1.1") == -1
    assert sol.compareVersion("01", "1") == 0
    assert sol.compareVersion("1.1", "1.10") == -1

