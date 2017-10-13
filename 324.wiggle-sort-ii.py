#
# [324] Wiggle Sort II
#
# https://leetcode.com/problems/wiggle-sort-ii
#
# Medium (26.10%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,5,1,1,6,4]'
#
# 
# ⁠   Given an unsorted array nums, reorder it such that
# ⁠   nums[0] < nums[1] > nums[2] < nums[3]....
# 
# 
# 
# ⁠   Example:
# ⁠   (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5,
# 1, 6]. 
# ⁠   (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3,
# 1, 2].
# 
# 
# 
# ⁠   Note:
# ⁠   You may assume all input has valid answer.
# 
# 
# 
# ⁠   Follow Up:
# ⁠   Can you do it in O(n) time and/or in-place with O(1) extra space?
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
import heapq
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        nlogn complexity:
        if not nums:
            return
        nums = sorted(nums)
        idx1, idx2 = 1, 1
        n = len(nums)
        while idx1 <= idx2 < n:
            while idx2 < n-1 and nums[idx2] <= nums[idx1]:
                idx2 += 1
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
            idx1 += 2
            idx2 = idx1
        """
        n = len(nums)
        isOdd = (n & 1)
        mid = (n//2) + isOdd
        heap = list(nums)
        heapq.heapify(heap)
        median = float(0)
        while mid > 0:
            median = heapq.heappop(heap)
            mid -= 1
        if isOdd == 0:
            median = float((median+heapq.heappop(heap)) / 2)

        def wire(p):
            return (1+(2*p)) % (n|1)

        i, j = 0, 0
        k = n-1
        while j <= k:
            if nums[wire(j)] > median:
                nums[wire(i)], nums[wire(j)] = nums[wire(j)], nums[wire(i)]
                i += 1
                j += 1
            elif nums[wire(j)] < median:
                nums[wire(j)], nums[wire(k)] = nums[wire(k)], nums[wire(j)]
                k -= 1
            else:
                j += 1
            print(i,j,k,nums)





if __name__ == "__main__":
    s = Solution()
    t = [1, 5, 1, 1, 6, 4]
    s.wiggleSort(t)
    print(t)
