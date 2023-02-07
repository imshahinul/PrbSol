class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        ctr = Counter(arr)
        ctr1 = sorted(ctr, key=abs)
        for i in ctr1:
            if ctr[i] > ctr[i*2]:
                return False
            ctr[i*2] -= ctr[i]
        return True