class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        out = []
        smallCharFreq = sorted([w.count(min(w)) for w in words])

        for q in queries:
            cnt = q.count(min(q))
            idx = bisect.bisect(smallCharFreq, cnt)
            out.append(len(words) - idx)

        return out