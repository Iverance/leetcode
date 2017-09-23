class Solution():
    def getParentId(self, h, q, isRoot=True):
        print(h, q)
        if 2**h - 1 == q:
            if isRoot:
                return -1
            return 2**(h+1) - 1
        if 2**(h-1) - 1 == q or 2**h - 2 == q:
            return 2**h - 1
        if q < 2**(h-1):
            return self.getParentId(h-1, q, False)
        else:
            return self.getParentId(h-1, q-(2**(h-1)-1), False) + (2**(h-1)-1)
    def solveFluxIon(self, h, q):
        result = []
        for node in q:
            result.append(self.getParentId(h, node, True))
        print(result)
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.solveFluxIon(3, [7, 2, 3, 5, 1]) ==  [-1, 3, 7, 6, 3]




        
