#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii
#
# Medium (46.96%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,1]'
#
# 
# Given a circular array (the next element of the last element is the first
# element of the array), print the Next Greater Number for every element. The
# Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, output -1 for this
# number.
# 
# 
# Example 1:
# 
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find
# next greater number; The second 1's next greater number needs to search
# circularly, which is also 2.
# 
# 
# 
# Note:
# The length of given array won't exceed 10000.
# 
#
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack = []
        result = [-1 for _ in range(n)]
        for i in range(n*2):
            num = nums[i%n]
            while stack and num > nums[stack[-1]]:
                pre = stack.pop()
                result[pre] = num
            stack.append(i%n)
        return result 
if __name__ == "__main__":
    s = Solution()
    assert s.nextGreaterElements([1, 3, 4, 2]) == [3,4,-1,3]
    assert s.nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100]) == [120,11,120,120,123,123,-1,100,100,100]
