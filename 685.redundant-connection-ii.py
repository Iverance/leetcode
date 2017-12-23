#
# [685] Redundant Connection II
#
# https://leetcode.com/problems/redundant-connection-ii
#
# algorithms
# Hard (28.53%)
# Total Accepted:    2.5K
# Total Submissions: 8.8K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 
# In this problem, a rooted tree is a directed graph such that, there is
# exactly one node (the root) for which all other nodes are descendants of this
# node, plus every node has exactly one parent, except for the root node which
# has no parents.
# 
# The given input is a directed graph that started as a rooted tree with N
# nodes (with distinct values 1, 2, ..., N), with one additional directed edge
# added.  The added edge has two different vertices chosen from 1 to N, and was
# not an edge that already existed.
# 
# The resulting graph is given as a 2D-array of edges.  Each element of edges
# is a pair [u, v] that represents a directed edge connecting nodes u and v,
# where u is a parent of child v.
# 
# Return an edge that can be removed so that the resulting graph is a rooted
# tree of N nodes.  If there are multiple answers, return the answer that
# occurs last in the given 2D-array.
# Example 1:
# 
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
# ⁠ 1
# ⁠/ \
# v   v
# 2-->3
# 
# 
# Example 2:
# 
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5 <- 1 -> 2
# ⁠    ^    |
# ⁠    |    v
# ⁠    4 <- 3
# 
# 
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is
# the size of the input array.
# 
#
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        r_graph = {}
        cndts = []
        for idx, edge in enumerate(edges):
            parent, child = edge
            if parent not in graph:     graph[parent] = []
            if child not in r_graph:    r_graph[child] = []
            graph[parent].append(child)
            r_graph[child].append(edge)
            if len(r_graph[child]) > 1:
                cndts = child
        #print(cndts, r_graph)
        cycle = self.hasCycle(graph, edges[0][0], [], [])
        if not cycle:
            return r_graph[cndts][-1]
        else:
            #print('has cycle', cycle)
            for i in range(len(edges)-1, -1, -1):
                u, v = edges[i]
                if cndts and v != cndts:
                    continue
                if all(v in cycle for v in edges[i]):
                    return edges[i]
            return True

    def hasCycle(self, graph, u, stack, visited):
        stack.append(u)
        visited.append(u)
        for child in graph.get(u,[]):
            if child not in visited:
                if self.hasCycle(graph, child, stack, visited):
                    return stack
            elif child in stack:
                return stack

        stack.pop()
        return []
        
