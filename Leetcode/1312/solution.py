class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        bucket = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    bucket[i][j] = bucket[i + 1][j - 1]
                else:
                    bucket[i][j] = min(bucket[i + 1][j], bucket[i][j - 1]) + 1
        return bucket[0][-1]