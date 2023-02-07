class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        closest = sum(nums[0:3])
        for i in range(l - 2):
            j = i + 1
            k = l - 1
            while(j < k):
                temp = nums[i] + nums[j] + nums[k]
                if temp == target:
                    return temp
                d = temp - target
                if abs(temp - target) < abs(closest - target):
                    closest = temp
                elif temp < target:
                    j += 1
                elif temp > target:
                    k -= 1
        return closest