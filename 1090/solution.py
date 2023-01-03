class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        out = 0
        labels_used = collections.defaultdict(int)
        items = sorted(zip(values, labels))
        while numWanted and items:
            v, l = items.pop()
            if labels_used[l] < useLimit:
                labels_used[l] += 1
                numWanted -= 1
                out += v
        return out