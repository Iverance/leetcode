#
# [380] Insert Delete GetRandom O(1)
#
# https://leetcode.com/problems/insert-delete-getrandom-o1
#
# Medium (39.16%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n[[],[1],[2],[2],[],[1],[2],[]]'
#
# Design a data structure that supports all following operations in average
# O(1) time.
# 
# 
# 
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each
# element must have the same probability of being returned.
# 
# 
# 
# Example:
# 
# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();
# 
# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);
# 
# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);
# 
# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);
# 
# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();
# 
# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);
# 
# // 2 was already in the set, so return false.
# randomSet.insert(2);
# 
# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();
# 
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = {}
        self.arr = []
        self.size = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            self.index[val] = self.size
            self.arr.append(val)
            self.size += 1
            return True
        else:
            return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            self.size -= 1
            idx = self.index[val]
            
            lastVal = self.arr[self.size]
            self.arr[idx] = lastVal
            self.index[lastVal] = idx
            
            del self.index[val]
            self.arr.pop()
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, self.size - 1)
        return self.arr[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
