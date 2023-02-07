class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        out = []
        counters = [[] for _ in range(len(words) + 1)]

        for word, cnt in Counter(words).items():
            counters[cnt].append(word)

        for c in reversed(counters):
            for word in sorted(c):
                out.append(word)
                if len(out) == k:
                    return out