class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        single, center, pair = 0, 0, 0
        ctr = Counter(words)

        for word, cnt in ctr.items():
            if word[0] == word[1]:
                single += cnt // 2 * 2
                if cnt % 2 == 1:
                    center = 2
            else:
                pair += min(ctr[word], ctr[word[::-1]]) * 0.5

        return single * 2 + int(pair) * 4 + center