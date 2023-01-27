class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_arr = sorted(words, key=lambda w: len(w))
        words_set = set(words)
        words_len = [len(words_arr[0])]
        for w in words_arr:
            if len(w) > words_len[-1]:
                words_len.append(len(w))

        def backtrack(w, la):
            for ll in la[-1::-1]:
                if w[:ll] in words_set:
                    nw = w[ll:]
                    if nw in words_set:
                        return True
                    nll = bisect_right(la, len(nw))
                    if nll > 0:
                        if backtrack(nw, la[:nll]):
                            return True
            return False

        out = []
        for w in words_arr[-1::-1]:
            if len(w) == words_len[-1]:
                words_len.pop()
                if len(words_len) == 0:
                    return out
            if backtrack(w, words_len):
                out.append(w)
        return out