class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        bucket = [[0] * n for _ in range(n)]
        print(bucket)
        for i in reversed(range(n)):
            for j in range(i, n):
                if i == j:
                    bucket[i][j] = piles[i]
                else:
                    bucket[i][j] = max(piles[i] - bucket[i + 1][j], piles[j] - bucket[i][j - 1])
        return bucket[0][n - 1] > 0

