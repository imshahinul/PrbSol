class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        l = len(arr)
        out = []
        for i in range(l):
            target = max(arr[0:l-i])
            j = 0
            while arr[j] != target:
                j += 1
            arr[:j+1] = reversed(arr[:j+1])
            out.append(j+1)
            arr[:l-i] = reversed(arr[:l-i])
            out.append(l-i)
        return out