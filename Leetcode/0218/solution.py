class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        out = []
        i, n = 0, len(buildings)
        h = []
        while i < n or h:
            if not h or i < n and buildings[i][0] <= -h[0][1]:
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heapq.heappush(h, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                x = -h[0][1]
                while h and -h[0][1] <= x:
                    heapq.heappop(h)
            height = len(h) and -h[0][0]
            if not out or height != out[-1][1]:
                out += [x, height],
        return out