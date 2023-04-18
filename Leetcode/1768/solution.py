class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ''
        ml = min(len(word1),len(word2))
        for i in range(ml):
            out += word1[i] + word2[i]
        out += word1[ml:] + word2[ml:]
        return out