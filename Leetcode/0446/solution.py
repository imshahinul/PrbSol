class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        bucket = [defaultdict(int) for _ in range(len(nums))]
        out = 0
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[j] - nums[i]
                out += bucket[j][diff]
                bucket[i][diff] += bucket[j][diff] + 1
        return out