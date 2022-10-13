class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        out = 0
        for i in range(len(difficulty)):
            difficulty[i] = (difficulty[i], profit[i])
        difficulty.sort(key = lambda x:x[0])
        i = 0
        ln = len(difficulty)
        max_p = 0
        for w in sorted(worker):
            while i < ln and difficulty[i][0] <= w:
                max_p = max(max_p,difficulty[i][1])
                i += 1
            out += max_p
        return out