class Solution:
    def reorganizeString(self, s: str) -> str:
        s1 = sorted(sorted(s), key=s.count)
        m = len(s1) // 2
        s1[1::2], s1[::2] = s1[:m], s1[m:]
        return "".join(s1) if s1[-1:] != s1[-2:-1] else ""