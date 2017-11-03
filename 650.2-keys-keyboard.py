#
# [650] 2 Keys Keyboard
#
# https://leetcode.com/problems/2-keys-keyboard
#
# Medium (43.21%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '3'
#
# 
# Initially on a notepad only one character 'A' is present. You can perform two
# operations on this notepad for each step: 
# 
# Copy All: You can copy all the characters present on the notepad (partial
# copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# 
# 
# 
# 
# Given a number n. You have to get exactly n 'A' on the notepad by performing
# the minimum number of steps permitted. Output the minimum number of steps to
# get n 'A'. 
# 
# 
# Example 1:
# 
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# 
# 
# 
# 
# Note:
# 
# The n will be in the range [1, 1000].
# 
# 
#
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        Same idea but doing trick here. Since we are always finding n's factor,
        and dividing by factor will reduce the problem, we iterate from 2 and finding 
        all the best way to make n/n's factors decrease fastest.
        """
        minV = 0
        for i in range(2,n+1):
            while n%i == 0:
                minV += i
                n /= i
        return minV
        """
        DP solution for same idea:
        dp = [x for x in range(n+1)]
        for i in range(2,n+1):
            for j in range(2,i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)
        return dp[n]
        
        Recursion solution:
        Since target n can be divided to small chunk in clipboard,
        we get the steps of small size clipboard and copy+paste(target/clipboard)-1 times
        formula: stepsOfChunk + 1(Copy) - 1(currChunk@editor) + target/chunk(paste)
        if n == 1:
            return 0
        minV = n
        for i in range(2,n):
            if n % i == 0:
                minV = min(minV, self.minSteps(i) + n//i)
        return minV
        
        large depth recursion solution
        if not n:
            return 0
        self.minStep = float('inf')
        def write(clipBoard, steps, curr):
            if curr > n:
                return
            if curr == n:
                self.minStep = min(self.minStep, steps)
                return
            #copy and paste
            write(curr, steps+2, curr*2)
            #just paste
            if clipBoard > 0:
                write(clipBoard, steps+1, curr+clipBoard)
            
        write(0, 0, 1)
        return self.minStep
        """
    
if __name__ == "__main__":
    s = Solution()
    assert s.minSteps(3) == 3
