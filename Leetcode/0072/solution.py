class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        bucket = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            bucket[i][0] = i
        for j in range(n + 1):
            bucket[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    bucket[i][j] = bucket[i - 1][j - 1]
                else:
                    bucket[i][j] = min(bucket[i][j - 1], bucket[i - 1][j], bucket[i - 1][j - 1]) + 1
        return bucket[-1][n]