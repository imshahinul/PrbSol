class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        @cache
        def sub(i, j):
            if i >= m:
                return 1
            if j >= n:
                return 0
            out = sub(i, j + 1) + sub(i + 1, j + 1) * bucket[j][ord(target[i]) - ord("a")]
            return out % 1000000007

        m = len(target)
        n = len(words[0])
        bucket = [[0] * 26 for _ in range(n)]
        for w in words:
            for j, c in enumerate(w):
                bucket[j][ord(c) - ord("a")] += 1
        return sub(0, 0)