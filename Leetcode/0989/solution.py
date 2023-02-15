class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i, cf = len(num) - 1, 0
        out = []
        while i >= 0 or k or cf:
            cf += (0 if i < 0 else num[i]) + (k % 10)
            cf, v = divmod(cf, 10)
            out.append(v)
            k //= 10
            i -= 1
        return out[::-1]