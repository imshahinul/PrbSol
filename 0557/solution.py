class Solution:
    def reverseWords(self, s: str) -> str:
        out = []
        for word in s.split(' '):
            out.append((word[::-1]))
        return ' '.join(out)