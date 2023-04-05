class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        out = -inf
        p_s = [0 for i in range(len(nums))]
        p_s[0] = nums[0]
        for i in range(1, len(nums)):
            p_s[i] = p_s[i - 1] + nums[i]
        for i in range(len(nums)):
            out = max(out, (p_s[i] + i)// (i + 1))
            print(out)
        return out