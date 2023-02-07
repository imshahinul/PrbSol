class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs1 = sorted(pairs,key=lambda x:x[1])
        c = 0
        y_f = -math.inf
        for x,y in pairs1:
            if x > y_f:
                y_f = y
                c += 1
        return c