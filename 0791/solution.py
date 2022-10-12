class Solution:
    def customSortString(self, order: str, s: str) -> str:
        out = ''
        bucket = [0] * 26
        for ch in s:
            bucket[ord(ch) - ord('a')] += 1

        for ch in order:
            while bucket[ord(ch) - ord('a')] > 0:
                out += ch
                bucket[ord(ch) - ord('a')] -= 1

        for ch in 'abcdefghijklmnopqrstuvwxyz':
            for _ in range(bucket[ord(ch) - ord('a')]):
                out += ch

        return out