#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed
#
# Hard (28.76%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]\n[[],[1],[1],[2],[],[1],[]]'
#
# Design a data structure that supports all following operations in average
# O(1) time.
# Note: Duplicate elements are allowed.
# 
# 
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The
# probability of each element being returned is linearly related to the number
# of same value the collection contains.
# 
# 
# 
# Example:
# 
# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();
# 
# // Inserts 1 to the collection. Returns true as the collection did not
# contain 1.
# collection.insert(1);
# 
# // Inserts another 1 to the collection. Returns false as the collection
# contained 1. Collection now contains [1,1].
# collection.insert(1);
# 
# // Inserts 2 to the collection, returns true. Collection now contains
# [1,1,2].
# collection.insert(2);
# 
# // getRandom should return 1 with the probability 2/3, and returns 2 with the
# probability 1/3.
# collection.getRandom();
# 
# // Removes 1 from the collection, returns true. Collection now contains
# [1,2].
# collection.remove(1);
# 
# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();
# 
# 
#
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = {}
        self.arr = []
        self.size = 0
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        isContain = val in self.index
        if isContain:
            self.index[val].add(self.size)
        else:
            self.index[val] = set([self.size])
            
        self.arr += val,
        self.size += 1
        return not isContain
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            self.size -= 1
            
            idx = self.index[val].pop()
            
            if not self.index[val]:
                del self.index[val]
                
            # SWAP element if last element is not val
            if idx != self.size:
                lastVal = self.arr[self.size]
                self.arr[idx] = lastVal
                self.index[lastVal].remove(self.size)
                self.index[lastVal].add(idx)
            
            self.arr.pop()
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        idx = random.randint(0, self.size - 1)
        return self.arr[idx]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
