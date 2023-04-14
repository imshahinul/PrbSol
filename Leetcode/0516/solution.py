class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        bucket = [[0] * n for _ in range(n)]

        for i in range(n):
            bucket[i][i] = 1

        for j in range(1, n):
            for k in range(n - j):
                l = k + j
                if s[k] == s[l]:
                    bucket[k][l] = 2 + bucket[k + 1][l - 1]
                else:
                    bucket[k][l] = max(bucket[k + 1][l], bucket[k][l - 1])

        return bucket[0][n - 1]