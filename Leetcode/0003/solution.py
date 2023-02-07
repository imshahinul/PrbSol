class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = 0
        dd = defaultdict(int)

        l = 0
        for i, c in enumerate(s):
            dd[c] += 1
            while dd[c] > 1:
                dd[s[l]] -= 1
                l += 1
            out = max(out, i - l + 1)

        return out