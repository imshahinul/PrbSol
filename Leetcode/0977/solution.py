class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        out = [0] * n

        while n:
            n -= 1
            if abs(nums[left]) > abs(nums[right]):
                out[n] = nums[left] * nums[left]
                left += 1
            else:
                out[n] = nums[right] * nums[right]
                right -= 1

        return out