class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subseq(x, y):
            it = iter(y)
            return all(c in it for c in x)

        cnt = 0
        ctr = {}
        for word in words:
            if word not in ctr:
                if is_subseq(word, s):
                    cnt += 1
                    ctr[word] = 1
                else:
                    ctr[word] = 0
            else:
                if ctr[word]:
                    cnt += 1

        return cnt