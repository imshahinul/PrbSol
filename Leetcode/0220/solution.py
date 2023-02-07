class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff == 0 and len(nums) == len(set(nums)):
            return False
        if indexDiff == 0 or valueDiff < 0:
            return False
        container = {}
        n = len(nums)
        for i in range(n):
            j = nums[i] // (valueDiff + 1)
            if j in container:
                return True
            if j - 1 in container:
                if abs(nums[i] - container[j - 1]) <= valueDiff:
                    return True
            if j + 1 in container:
                if abs(nums[i] - container[j + 1]) <= valueDiff:
                    return True
            if i >= indexDiff:
                del container[nums[i - indexDiff] // (valueDiff + 1)]
            container[j] = nums[i]
        return False