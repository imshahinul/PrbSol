class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ln = len(s)
        max_len = len(max(wordDict, key=len))
        word_map = set(wordDict)

        bucket = [True] + [False] * ln
        for i in range(1, ln + 1):
            for j in reversed(range(i)):
                if max_len < i - j:
                    break
                if bucket[j] and s[j:i] in word_map:
                    bucket[i] = True
                    break

        return bucket[ln]