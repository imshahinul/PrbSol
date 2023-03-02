class Solution:
    def compress(self, chars: List[str]) -> int:
        l, s, n = 0, 0, len(chars)
        while l < n:
            m = l + 1
            while m < n and chars[m] == chars[l]:
                m += 1
            chars[s] = chars[l]
            s += 1
            if m - l > 1:
                cnt = str(m - l)
                for c in cnt:
                    chars[s] = c
                    s += 1
            l = m
        return s