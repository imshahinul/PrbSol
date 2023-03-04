class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        out, lowest, highest, inbetween = 0, -1, -1, -1
        for idx, num in enumerate(nums):
            if num < minK or num > maxK:
                inbetween = idx
            if num == minK:
                lowest = idx
            if num == maxK:
                highest = idx
            out += max(0, min(lowest, highest) - inbetween)
        return out