class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [[p,s] for p,s in zip(position,speed)]
        fleets = []
        for p,s in reversed(sorted(position_speed)):
            fleets.append((target - p)/s)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        return len(fleets)