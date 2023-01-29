class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set()
        for i in range(len(nums)):
            if i > k:
                visited.remove(nums[i - k - 1])
            if nums[i] in visited:
                return True
            visited.add(nums[i])
        return False