#
# [384] Shuffle an Array
#
# https://leetcode.com/problems/shuffle-an-array
#
# Medium (46.66%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
#
# Shuffle a set of numbers without duplicates.
# 
# 
# Example:
# 
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
# 
# // Shuffle the array [1,2,3] and return its result. Any permutation of
# [1,2,3] must equally likely to be returned.
# solution.shuffle();
# 
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
# 
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
# 
# 
#
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums
        self.n = len(nums)        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.arr

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        size = self.n - 1
        s = list(self.arr)
        while size != -1:
            idx = random.randint(0,size)
            s.append(s.pop(idx))
            size -= 1
        return s


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
