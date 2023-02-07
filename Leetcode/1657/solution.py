class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        ctr1 = Counter(word1)
        ctr2 = Counter(word2)

        if ctr1.keys() != ctr2.keys():
            return False

        return sorted(ctr1.values()) == sorted(ctr2.values())