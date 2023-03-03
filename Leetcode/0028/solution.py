class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = len(needle)
        n = len(haystack)
        for i in range(n - s + 1):
            if haystack[i:i + s] == needle:
                return i
        return -1