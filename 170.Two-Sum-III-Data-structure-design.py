"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []


    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        import bisect
        insrt = bisect.bisect_left(self.arr, number)
        self.arr.insert(insrt, number)
        # print(self.arr)


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        left, right = 0, len(self.arr)-1
        while left<right:
            tot = self.arr[left] + self.arr[right]
            if tot == value:
                return True
            elif tot < value:
                left += 1
            else:
                right -= 1
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
