class Solution:
    def minJumps(self, arr: List[int]) -> int:
        g = defaultdict(list)
        for idx, a in enumerate(arr):
            g[a].append(idx)
        dq = deque([(0, 0)])
        traversed = {0}
        while dq:
            idx, dis = dq.popleft()
            if idx == len(arr) - 1:
                return dis
            a = arr[idx]
            dis += 1
            for j in g[a]:
                if j not in traversed:
                    traversed.add(j)
                    dq.append((j, dis))
            del g[a]
            if idx + 1 < len(arr) and (idx + 1) not in traversed:
                traversed.add(idx + 1)
                dq.append((idx + 1, dis))
            if idx - 1 >= 0 and (idx - 1) not in traversed:
                traversed.add(idx - 1)
                dq.append((idx - 1, dis))