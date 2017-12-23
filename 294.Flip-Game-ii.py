"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
"""
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        n = len(s)
        endCase = set()

        def backTrack(seq):
            if seq in endCase:
                return False
            mayWin = False
            for i in range(1,len(seq)):
                if seq[i] == '+' and seq[i]==seq[i-1]:
                    mayWin = mayWin or not backTrack(seq[:i-1]+'--'+seq[i+1:])
            if not mayWin:
                endCase.add(seq)
            return mayWin

        return backTrack(s)
