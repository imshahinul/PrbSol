class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subseq(x, y):
            it = iter(y)
            return all(c in it for c in x)

        dictionary.sort(key=lambda x: (-len(x), x))

        for word in dictionary:
            if is_subseq(word, s):
                return word
        return ''