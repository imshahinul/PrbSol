class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ctr = Counter(arr).most_common()
        ctr.sort(key=lambda x: -x[1])
        total = 0
        for i,k in enumerate(ctr):
            total += k[1]
            if total >= len(arr) // 2:
                return i + 1