#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion
#
# Medium (26.64%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""\n1'
#
# 
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# string convert(string text, int nRows);
# 
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
# 
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 0 or numRows == 1:
            return s
        lines = [[] for _ in range(numRows)]
        isDown,rowN = False,0
        for idx, ch in enumerate(s):
            #print(rowN)
            lines[rowN].append(ch)
            if idx % (numRows-1) == 0:
                isDown = not isDown
            rowN += 1 if isDown else (-1)
        result = ""
        for line in lines:
            result += "".join(line)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
    print(sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
    print(sol.convert("PAYPALISHIRING", 0) == "PAYPALISHIRING")
    print(sol.convert("PAYPALISHIRING", 1) == "PAYPALISHIRING")
            
