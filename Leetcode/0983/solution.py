class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        out = 0
        t2 = deque()
        t3 = deque()

        for day in days:
            while t2 and t2[0][0] + 7 <= day:
                t2.popleft()
            while t3 and t3[0][0] + 30 <= day:
                t3.popleft()
            t2.append([day, out + costs[1]])
            t3.append([day, out + costs[2]])
            out = min(out + costs[0], t2[0][1], t3[0][1])

        return out