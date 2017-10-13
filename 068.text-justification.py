#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification
#
# Hard (19.19%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[""]\n0'
#
# 
# Given an array of words and a length L, format the text such that each line
# has exactly L characters and is fully (left and right) justified.
# ⁠
# 
# 
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly L characters.
# 
# 
# 
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the
# right.
# 
# 
# 
# For the last line of text, it should be left justified and no extra space is
# inserted between words.
# 
# 
# 
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
# 
# 
# 
# Return the formatted lines as:
# 
# [
# ⁠  "This    is    an",
# ⁠  "example  of text",
# ⁠  "justification.  "
# ]
# 
# 
# 
# 
# Note: Each word is guaranteed not to exceed L in length.
# 
# 
# 
# click to show corner cases.
# 
# Corner Cases:
# 
# 
# A line other than the last line might contain only one word. What should you
# do in this case?
# In this case, that line should be left-justified.
# 
# 
#
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            words.append("")
        n = len(words)
        i = 0
        result = []
        while i < n:
            line = []
            wordCnt = 0
            while i < n and wordCnt+len(line)+len(words[i]) <= maxWidth:
                line.append(words[i])
                wordCnt += len(words[i])
                i += 1
            #last line
            if i >= n: 
                newLine = ' '.join(line)
                while len(newLine) < maxWidth:
                    newLine += ' '
            else:
                spaceCnt = maxWidth - wordCnt
                if len(line) == 1:
                    newLine = line[0] + ' ' * spaceCnt
                else:
                    q, r = divmod(spaceCnt, len(line)-1)
                    space = ' ' * q
                    newLine = ''
                    for w in line:
                        newLine += w
                        if len(newLine) < maxWidth:
                            newLine += space
                        if r > 0:
                            newLine += ' '
                            r -= 1
            result.append(newLine)
            #print('"'+newLine+'"')
        return result
if __name__ == '__main__':
    s = Solution()
    assert s.fullJustify([],2) == ["  "]
    assert s.fullJustify([""],2) == ["  "]
    assert s.fullJustify(["",""],2) == ["  "]
    assert s.fullJustify(["a"],1) == ["a"]
    assert s.fullJustify(["a","b","c","d","e"],3) == ["a b","c d","e  "]
    assert s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
