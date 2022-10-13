class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        str_map = {}
        for i in range(len(sources)):
            if s.find(sources[i], indices[i]) == indices[i]:
                str_map[indices[i]] = (sources[i], targets[i])
        s1 = ''
        k = 0
        while k < len(s):
            s1 += k in str_map and str_map[k][1] or s[k]
            k += k in str_map and len(str_map[k][0]) or 1
        return s1