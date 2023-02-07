class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for i in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        stk = [source]
        traversed = set(stk)
        while stk:
            pointer = stk.pop()
            if pointer == destination:
                return True
            for p in adj[pointer]:
                if p not in traversed:
                    stk.append(p)
                    traversed.add(p)
        return False