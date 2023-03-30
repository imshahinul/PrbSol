class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        l = len(s1)
        bucket = [[[False] * (l + 1) for _ in range(l)] for _ in range(l)]
        for i in range(l):
            for j in range(l):
                bucket[i][j][1] = s1[i] == s2[j]
        for m in range(2, l + 1):
            for n in range(l - m + 1):
                for o in range(l - m + 1):
                    for i in range(1, m):
                        if bucket[n][o][i] and bucket[n + i][o + i][m - i]:
                            bucket[n][o][m] = True
                            break
                        if bucket[n][o + m - i][i] and bucket[n + i][o][m - i]:
                            bucket[n][o][m] = True
                            break
        return bucket[0][0][l]