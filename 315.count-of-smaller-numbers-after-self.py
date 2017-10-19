#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self
#
# Hard (34.54%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[5,2,6,1]'
#
# 
# You are given an integer array nums and you have to return a new counts
# array.
# The counts array has the property where counts[i] is 
# the number of smaller elements to the right of nums[i].
# 
# 
# Example:
# 
# 
# Given nums = [5, 2, 6, 1]
# 
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
# 
# 
# Return the array [2, 1, 1, 0].
# 
#
from heapq import heapify, heappop, heappush
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0 for _ in range(n)]
        t = []
        for i in range(n-1, -1, -1):
            l, r = 0, len(t)
            while l < r:
                mid = l+((r-l)//2)
                if t[mid] >= nums[i]:
                    r = mid 
                else:
                    l = mid + 1
            res[i] = r
            t.insert(r, nums[i])
            #print(t)
        return res

        """
        TLE Solution
        if not nums:
            return []
        big = []
        small = []
        res = []
        for num in nums:
            heappush(big, num)
        for num in nums:
            while big and num > big[0]:
                heappush(small, -heappop(big))
            while small and -small[0] >= num:
                heappush(big, -heappop(small))
            print(big,small)
            res.append(len(small))
            heappop(big)
        return res
        """
if __name__ == "__main__":
    s = Solution()
    print(s.countSmaller([5,2,6,1]))
    print(s.countSmaller([2,0,1]))

        
