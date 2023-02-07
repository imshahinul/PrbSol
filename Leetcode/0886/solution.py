class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        edge = [[] for _ in range(n+1)]
        for u, v in dislikes:
            edge[u].append(v)
            edge[v].append(u)
        color = [0] * (n+1)
        for i in range(0, n):
            if color[i] == 0:
                q = [i]
                color[i] = 1
                while q:
                    cur = q.pop()
                    cur_c = color[cur]
                    for node in edge[cur]:
                        if color[node] == 0:
                            color[node] = cur_c * -1
                            q.append(node)
                        elif color[node] == cur_c:
                            return False
        return True