class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        out = 0
        s = str(num)
        for i in range(len(s) - k + 1):
            t = int(s[i : i + k])
            if t and num % t == 0:
                out += 1
        return out