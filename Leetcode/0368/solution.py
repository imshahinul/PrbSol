class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        buckets = [[None, i] for i in range(len(nums))]
        index = max_ln = 0
        for i, num in enumerate(nums):
            z = 0
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if z < buckets[j][0]:
                        z = buckets[j][0]
                        buckets[i][1] = j
            buckets[i][0] = z + 1
            if buckets[i][0] > max_ln:
                max_ln = buckets[i][0]
                index = i
        out = [nums[index]]
        while index != buckets[index][1]:
            index = buckets[index][1]
            out.append(nums[index])
        return out[::-1]