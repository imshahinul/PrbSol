class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        return [*map(pattern.index, pattern)] == [*map(words.index, words)]