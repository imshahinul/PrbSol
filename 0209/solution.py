class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        out = math.inf
        summation = 0
        k = 0

        for i, num in enumerate(nums):
            summation += num
            while summation >= s:
                out = min(out, i - k + 1)
                summation -= nums[k]
                k += 1

        return out if out != math.inf else 0