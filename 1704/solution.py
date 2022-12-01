class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum(list(map(s[:len(s)//2].lower().count, "aeiou"))) == sum(list(map(s[len(s)//2:].lower().count, "aeiou")))