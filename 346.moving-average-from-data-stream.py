class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        from collections import deque
        self.q = deque()
        self.size = size
        self.total = 0
        
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.q) == self.size:
            self.total -= self.q.popleft()
        self.q.append(val)
        self.total += val
        return self.total / len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
