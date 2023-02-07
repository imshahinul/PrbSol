class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        out = []
        n = len(tasks)
        min_heap = []
        indexed_tasks = [[*task, i] for i, task in enumerate(tasks)]

        i = 0
        t = 0

        indexed_tasks.sort()

        while i < n or min_heap:
            if not min_heap:
                t = max(t, indexed_tasks[i][0])
            while i < n and t >= indexed_tasks[i][0]:
                heapq.heappush(min_heap, (indexed_tasks[i][1], indexed_tasks[i][2]))
                i += 1
            pt, ind = heapq.heappop(min_heap)
            t += pt
            out.append(ind)

        return out