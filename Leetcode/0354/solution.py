class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda k: (k[0], -k[1]))
        out = 0
        buckets = [None] * len(envelopes)
        for _, y in envelopes:
            i = 0
            j = out
            while i < j:
                k = (i + j) // 2
                if buckets[k] >= y:
                    j = k
                else:
                    i = k + 1
            buckets[i] = y
            if i == out:
                out += 1
        return out