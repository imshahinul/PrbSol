class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        out = 0
        curr = 0
        sm = 0

        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            sm += gas[i] - cost[i]
            if sm < 0:
                sm = 0
                out = i + 1

        return -1 if curr < 0 else out