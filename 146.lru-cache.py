#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache
#
# Hard (17.86%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# 
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
#
class LinkedNode:
    def __init__(self, k, v):
        self.val = v
        self.key = k
        self.pre = None
        self.next = None
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.size = 0
        self.d = {}
        self.head = LinkedNode(0, 0)
        self.tail = LinkedNode(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print(key)
        if key not in self.d:
            return -1
        val = self.d[key].val
        self.deleteNode(self.d[key])
        self.addNode(self.d[key])
        return val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print(key,value)
        if key not in self.d:
            if self.size == self.cap:                
                delKey = self.tail.pre.key
                self.deleteNode(self.d[delKey])
                del self.d[delKey]
                self.size -= 1
            node = LinkedNode(key, value)
            self.addNode(node)
            self.d[key] = node
            self.size += 1
        else:
            self.d[key].val = value
            self.deleteNode(self.d[key])
            self.addNode(self.d[key])
    
    def deleteNode(self, node):
        preNode = node.pre
        nextNode = node.next
        preNode.next, nextNode.pre = nextNode, preNode
    
    def addNode(self, node): 
        headNext = self.head.next
        self.head.next = node
        headNext.pre = node
        node.pre = self.head
        node.next = headNext
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
