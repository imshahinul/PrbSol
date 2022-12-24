class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_hashmap = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in str_hashmap:
                str_hashmap[ss] = []

            str_hashmap[ss].append(s)
        return str_hashmap.values()