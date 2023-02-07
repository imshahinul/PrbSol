class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        out = 0
        prefix = 0
        count = [1] + [0] * (k - 1)

        for num in nums:
            prefix = (prefix + num) % k
            out += count[prefix]
            count[prefix] += 1

        return out