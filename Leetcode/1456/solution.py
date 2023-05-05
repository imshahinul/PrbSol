class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vs = set('aeiou')
        temp = sum(ch in vs for ch in s[:k])
        out = temp
        # do slide
        for i in range(k, len(s)):
            temp += s[i] in vs
            temp -= s[i - k] in vs
            out = max(out, temp)
        return out