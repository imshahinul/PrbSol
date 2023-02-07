class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        jump = 0

        while i < n and i <= jump:
            jump = max(jump, i + nums[i])
            i += 1

        return i == n