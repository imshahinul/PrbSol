class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        bucket = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                if text1[i] == text2[j]:
                    bucket[i + 1][j + 1] = 1 + bucket[i][j]
                else:
                    bucket[i + 1][j + 1] = max(bucket[i][j + 1], bucket[i + 1][j])
        return bucket[l1][l2]