class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        out = None
        c = 0
        for num in nums:
            if c != 0:
                c += 1 if out == num else -1
            else:
                out = num
                c = 1
        return out if nums.count(out) > len(nums) // 2 else None