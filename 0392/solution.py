class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        buckets = [[0] * 26 for _ in range(len_t)]
        buckets.append([len_t]*26)
        for i in range(len_t-1,-1,-1):
            for j in range(26):
                if ord(t[i]) == j + ord('a'):
                    buckets[i][j] = i
                else:
                    buckets[i][j] = buckets[i+1][j]
        k = 0
        for q in range(len_s):
            if buckets[k][ord(s[q]) - ord('a')] == len_t:
                return False
            k = buckets[k][ord(s[q]) - ord('a')] + 1
        return True