class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if [*map(s.index, s)] == [*map(t.index, t)]:
            return True
        return False