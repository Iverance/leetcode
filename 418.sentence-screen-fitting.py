"""
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
"""
class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        wholeSentence = "-".join(sentence) + "-"
        idx, n = 0, len(wholeSentence)
        for m in range(rows):
            idx += cols
            if wholeSentence[idx%n] == '-':
                idx += 1
            else:
                while idx > 0 and wholeSentence[(idx-1)%n] != '-':
                    idx -= 1
        return idx//n

