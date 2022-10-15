class Solution:
    def check_equal(self, ctr: Dict[int, int]) -> bool:
        f = -1
        for ch in ctr.values():
            if ch == 0 or ch == f:
                continue
            if f == -1:
                f = ch
            else:
                return False
        return True

    def equalFrequency(self, word: str) -> bool:
        ctr = Counter(word)
        for ch in word:
            ctr[ch] -= 1
            if self.check_equal(ctr):
                return True
            ctr[ch] += 1

        return False