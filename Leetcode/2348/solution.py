class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        out, c = 0, 0
        for num in nums:
            c = 0 if num else c + 1
            out += c
        return out