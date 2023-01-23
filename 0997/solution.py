class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        bucket = [0] * (n + 1)

        for t, nt in trust:
            bucket[t] -= 1
            bucket[nt] += 1

        for i in range(1, n + 1):
            if bucket[i] == n - 1:
                return i

        return -1