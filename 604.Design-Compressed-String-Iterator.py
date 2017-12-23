"""
Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
"""
class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        n = len(compressedString)
        meta = []
        tmp, num = '', 0
        # or re.findAll('\D\d+', compressedString)
        for idx, ch in enumerate(compressedString):
            if ch in '0123456789':
                num *= 10
                num += int(ch)
                if idx == n-1 or compressedString[idx+1] not in '0123456789':
                    meta.append([tmp,num])
                    num = 0
                    tmp = ''
            else:
                tmp = tmp + ch
        #print(meta)
        self.s = meta
        self.idx = 0
        self.size = len(self.s)


    def next(self):
        """
        :rtype: str
        """
        if self.s:
            ch = self.s[0][0]
            self.s[0][1] -= 1
            if self.s[0][1] == 0:
                self.s.pop(0)
            return ch
        else:
            return ' '

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.s else False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
