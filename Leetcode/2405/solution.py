class Solution:
    def partitionString(self, s: str) -> int:
        out, used = 1, 0
        for ch in s:
            idx = ord(ch) - ord('a')
            if used >> idx & 1:
                used = 1 << idx
                out += 1
            else:
                used |= 1 << idx
        return out