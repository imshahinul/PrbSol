class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        out = 0
        dd = defaultdict(set)
        for idea in ideas:
            dd[idea[0]].add(idea[1:])

        prefixes = list(dd.keys())
        n = len(prefixes)
        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = prefixes[i], prefixes[j]
                s1, s2 = dd[p1], dd[p2]
                s = s1 & s2
                if p1 != p2:
                    out += 2 * (len(s2) - len(s)) * (len(s1) - len(s))
        return out