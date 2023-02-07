class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        min_prefix = min(strs,key=len)
        for i, ch in enumerate(min_prefix):
            for other in strs:
                if other[i] != ch:
                    return min_prefix[:i]
        return min_prefix