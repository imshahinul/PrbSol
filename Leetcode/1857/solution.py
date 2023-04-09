class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n, c, out = len(colors), 0, 1
        zeros = [0] * n
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            zeros[v] += 1
        dq = deque()
        bucket = [[0] * 26 for _ in range(n)]
        for idx, zero in enumerate(zeros):
            if zero == 0:
                dq.append(idx)
                ch = ord(colors[idx]) - ord('a')
                bucket[idx][ch] += 1
        while dq:
            idx = dq.popleft()
            c += 1
            for j in graph[idx]:
                zeros[j] -= 1
                if zeros[j] == 0:
                    dq.append(j)
                ch = ord(colors[j]) - ord('a')
                for k in range(26):
                    bucket[j][k] = max(bucket[j][k], bucket[idx][k] + (ch == k))
                    out = max(out, bucket[j][k])
        return -1 if c < n else out