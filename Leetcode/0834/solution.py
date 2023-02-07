class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = collections.defaultdict(list)
        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)

        dic = {i: [1, 0] for i in range(n)}

        def predfs(node, p):
            for k in tree[node]:
                if k != p:
                    predfs(k, node)
                    dic[node][0] += dic[k][0]
                    dic[node][1] += (dic[k][0] + dic[k][1])

        def postdfs(node, p):
            for k in tree[node]:
                if k != p:
                    dic[k][1] = dic[node][1] - dic[k][0] + (n - dic[k][0])
                    postdfs(k, node)

        predfs(0, -1)
        postdfs(0, -1)
        out = []
        for key in dic:
            out.append(dic[key][1])
        return out