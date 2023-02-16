class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        bucket = [[False] * n for _ in range(n)]
        start = 0
        end = 1
        for i in range(n):
            for j in range(i + 1):
                if i - j < 2:
                    bucket[j][i] = s[j] == s[i]
                else:
                    bucket[j][i] = bucket[j + 1][i - 1] and s[j] == s[i]
                if bucket[j][i] and end < i - j + 1:
                    start, end = j, i - j + 1
        return s[start: start + end]