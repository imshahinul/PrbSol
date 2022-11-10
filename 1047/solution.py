class Solution:
    def removeDuplicates(self, s: str) -> str:
        out = [] #stack
        for ch in s:
            if len(out) > 0 and out[-1] == ch:
                out.pop()
            else:
                out.append(ch)
        return("".join(out))