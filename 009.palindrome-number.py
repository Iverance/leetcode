#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number
#
# Easy (35.41%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '-2147483648'
#
# Determine whether an integer is a palindrome. Do this without extra space.
# 
# click to show spoilers.
# 
# Some hints:
# 
# Could negative integers be palindromes? (ie, -1)
# 
# If you are thinking of converting the integer to string, note the restriction
# of using extra space.
# 
# You could also try reversing an integer. However, if you have solved the
# problem "Reverse Integer", you know that the reversed integer might overflow.
# How would you handle such case?
# 
# There is a more generic way of solving this problem.
# 
# 
#
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original = x
        reverseInt = 0
        while x > 0:
            reverseInt *= 10
            reverseInt += (x%10)
            x /= 10
        return reverseInt == original
if __name__ == "__main__":
    s = Solution()
    s.isPalindrome(123454321) ==  True
    s.isPalindrome(0) == True
    s.isPalindrome(1) == True
    s.isPalindrome(-454) == False    
