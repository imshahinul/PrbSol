class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb, ub = 0, len(nums) - 1
        while lb < ub:
            mid = (lb + ub) // 2
            if nums[mid] >= target:
                ub = mid
            else:
                lb = mid + 1
        return lb if nums[lb] == target else -1