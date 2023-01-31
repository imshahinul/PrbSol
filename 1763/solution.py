class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        out = ''
        for j in range(n):
            lc = uc = 0
            for i in range(j, n):
                if s[i].islower():
                    lc |= 1 << (ord(s[i]) - ord('a'))
                else:
                    uc |= 1 << (ord(s[i]) - ord('A'))
                if lc == uc and len(out) < i - j + 1:
                    out = s[j: i + 1]
        return out