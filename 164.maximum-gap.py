#
# [164] Maximum Gap
#
# https://leetcode.com/problems/maximum-gap
#
# Hard (29.45%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given an unsorted array, find the maximum difference between the successive
# elements in its sorted form.
# 
# Try to solve it in linear time/space.
# 
# Return 0 if the array contains less than 2 elements.
# 
# You may assume all elements in the array are non-negative integers and fit in
# the 32-bit signed integer range.
# 
# Credits:Special thanks to @porker2008 for adding this problem and creating
# all test cases.
#
import math
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        M, m = max(nums), min(nums)
        buckLen = math.ceil(float(M - m)/(len(nums)-1))
        #print(buckLen)
        buckSize = ((M-m)//buckLen) + 1
        buckets = [[float('inf'), float('-inf')] for _ in range(int(buckSize))]
        for num in nums:
            idx = int((num-m)/buckLen)
            #print(idx, buckLen)
            if num < buckets[idx][0]:
                buckets[idx][0] = num
            if buckets[idx][1] < num:
                buckets[idx][1] = num

        p, q, gap = 0, 1, float('-inf')
        #print(buckets)
        while p < q < len(buckets):
            while p < q < len(buckets) and buckets[p][0] == float('inf'):
                p += 1
                q = p + 1
            while p < q < len(buckets) and buckets[q][0] == float('inf'):
                q += 1
            #print(p,q)
            gap = max(buckets[q][0] - buckets[p][1], gap)
            p = q
            q = p + 1
        #print(gap)
        return gap
if __name__ == "__main__":
    sol = Solution()
    assert sol.maximumGap([]) == 0
    assert sol.maximumGap([1,2,3,4,5,10,11,12,13]) == 5
    assert sol.maximumGap([1,2,3,4,5]) == 1
    assert sol.maximumGap([1,1,1,1,1]) == 0
    assert sol.maximumGap([1,1,1,1,2]) == 1
    assert sol.maximumGap([1,10000000]) == 9999999
