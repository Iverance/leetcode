"""
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button.
At the stage of rotating the ring to spell the key character key[i]:
You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.
"""

import collections
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        k_n = len(key)
        r_n = len(ring)
        memo = collections.defaultdict(int)
        def recur(r, idx):

            if (r,idx) in memo:
                return memo[(r,idx)]

            if idx == k_n:
                return 0

            right = left = 0
            # get next match clockwise
            while r[right] != key[idx]:
                right += 1
            # get next match counterclockwise
            while r[left%r_n] != key[idx]:
                left -= 1
            left %= r_n

            nextRightRing = r[right:] + r[:right]
            nextLeftRing = r[left:] + r[:left]

            res = min(recur(nextRightRing, idx+1)+right+1, recur(nextLeftRing, idx+1)+r_n-left+1)
            memo[(r,idx)] = res
            return res
        return recur(ring, 0)

