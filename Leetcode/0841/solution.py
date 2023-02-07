class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        traversed = [False] * len(rooms)
        def dfs(node):
            traversed[node] = True
            for key in rooms[node]:
                if not traversed[key]:
                    dfs(key)
        dfs(0)
        return all(traversed)