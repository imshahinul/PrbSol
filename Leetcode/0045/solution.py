class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = [0 for i in range(n)]

        jumps[0] = 0

        for i in range(1, n):
            jumps[i] = math.inf
            for j in range(i):
                if (i <= j + nums[j]) and (jumps[j] != math.inf):
                    jumps[i] = min(jumps[i], jumps[j] + 1)
                    break
        return jumps[n - 1]