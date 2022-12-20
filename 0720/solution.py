class Solution:
    def longestWord(self, words: List[str]) -> str:
        bucket = [chr(i+ ord('a')) for i in range(26)]
        lst = []
        for word in words:
            if len(word)==1:
                lst.append(word)
        word_set = set(words)
        out = ''
        while lst:
            rst = []
            for word in lst:
                for ch in bucket:
                    if word+ch in word_set:
                        rst.append(word+ch)
            if not rst:
                out = min(lst)
            lst = rst
        return out