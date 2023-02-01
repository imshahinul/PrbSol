class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wc = blocks[:k].count('W')
        out = wc
        i, n = k, len(blocks)
        while i < n:
            wc += blocks[i] == 'W'
            wc -= blocks[i - k] == 'W'
            out = min(out, wc)
            i += 1
        return out