class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        s = [*map(int, s)] + [math.inf]
        bucket = [0] * n + [1]
        for i in range(n, -1, -1):
            num, j = s[i], i + 1
            while 1 <= num <= k and j < n + 1:
                bucket[i] = (bucket[i] + bucket[j]) % 1000000007
                num = 10 * num + s[j]
                j += 1
        return bucket[0]