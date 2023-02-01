class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, out = set(), set()
        for l in range(len(s) - 9):
            sw = s[l:l + 10]
            if sw in seen:
                out.add(sw)
            seen.add(sw)
        return out