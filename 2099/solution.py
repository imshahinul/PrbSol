class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        out = []
        t = sorted(nums)[-k]
        l_sum = sum(num > t for num in nums)
        diff = k - l_sum

        for num in nums:
            if num > t:
                out.append(num)
            elif num == t and diff:
                out.append(num)
                diff -= 1
        return out