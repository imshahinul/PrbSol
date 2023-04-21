class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        bucket = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        for j in range(n + 1):
            bucket[0][j][0] = 1
        for idx, (g, p) in enumerate(zip(group, profit), 1):
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    bucket[idx][j][k] = bucket[idx - 1][j][k]
                    if j >= g:
                        bucket[idx][j][k] = (bucket[idx][j][k] + bucket[idx - 1][j - g][max(0, k - p)]) % 1000000007
        return bucket[m][n][minProfit]