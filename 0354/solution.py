class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda k: (k[0], -k[1]))
        c = 0
        buckets = [None] * len(envelopes)
        for x, y in envelopes:
            i = 0
            j = c
            while i < j:
                k = (i + j) // 2
                if buckets[k] >= y:
                    j = k
                else:
                    i = k + 1
            buckets[i] = y
            if i == c:
                c += 1
        return c