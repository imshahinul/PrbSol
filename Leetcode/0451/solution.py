class Solution:
    def frequencySort(self, s: str) -> str:
        c_map = Counter(s)
        buckets = [[] for i in range(len(s) + 1)]
        for c, f in c_map.items():
            buckets[f].append(c)

        out = []
        for f in reversed(range(len(buckets))):
            for c in buckets[f]:
                out.append(f * c)

        return ''.join(out)