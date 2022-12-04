class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        d = int(1e9 + 7)
        min_i = 0
        n = len(nums)
        splt = nums[:]; splt.append(0)
        for i in range(n - 1, -1, -1):
            splt[i] = nums[i] + splt[i + 1]
        for i in range(n):
            a = (splt[0] - splt[i + 1]) // (i + 1)
            b = (splt[i + 1] - splt[n]) // (n - 1 - i) if i + 1 < n else 0
            absd = abs(a - b)
            if d > absd:
                d = absd; min_i = i
        return min_i