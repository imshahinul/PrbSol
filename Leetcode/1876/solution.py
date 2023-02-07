class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        sw = list(s[:3])
        out = 1 if len(set(sw)) == 3 else 0

        for i in range(3, len(s)):
            sw.pop(0)
            sw.append(s[i])

            if len(set(sw)) == 3:
                out += 1

        return out