class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        out = []
        dict = {word[::-1]: i for i, word in enumerate(words)}

        for i, word in enumerate(words):
          if "" in dict and dict[""] != i and word == word[::-1]:
            out.append([i, dict[""]])

          for j in range(1, len(word) + 1):
            l = word[:j]
            r = word[j:]
            if l in dict and dict[l] != i and r == r[::-1]:
              out.append([i, dict[l]])
            if r in dict and dict[r] != i and l == l[::-1]:
              out.append([dict[r], i])

        return out