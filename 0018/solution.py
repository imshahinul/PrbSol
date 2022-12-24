class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quad = []
        if nums is None or len(nums) < 4:
            return quad
        nums.sort()
        v = len(nums)
        for i in range(0, v - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, v - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = v - 1
                while k < l:
                    temp = nums[i] + nums[j] + nums[k] + nums[l]
                    if temp < target:
                        k += 1
                    elif temp > target:
                        l -= 1
                    else:
                        quad.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
        return quad