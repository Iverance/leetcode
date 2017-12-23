#
# [246] Strobogrammatic Number
#
# https://leetcode.com/problems/strobogrammatic-number
#
# algorithms
# Easy (40.03%)
# Total Accepted:    30.6K
# Total Submissions: 76.5K
# Testcase Example:  '"1"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# Write a function to determine if a number is strobogrammatic. The number is
# represented as a string.
# For example, the numbers "69", "88", and "818" are all strobogrammatic.
#
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        table = {"6":"9", "8":"8", "9":"6", "1":"1", "0":"0"}
        left, right = 0, len(num)-1
        while left <= right:
            if num[left] not in table:
                return False
            if table[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
if __name__ == "__main__":
    s = Solution()
    assert s.isStrobogrammatic("818") == True
    assert s.isStrobogrammatic("69") == True
    assert s.isStrobogrammatic("659") == False
