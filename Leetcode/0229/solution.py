class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        out = set()
        n = len(nums)
        c_map = {}
        for num in nums:
            if num in c_map:
                c_map[num] = c_map[num] + 1
            else:
                c_map[num] = 1

            if c_map[num] > n / 3:
                out.add(num)
        return list(out)