class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0 : -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            if(k != 0):
                total = total % k
            if(total in hash_map):
                if(i-hash_map[total] > 1):
                    return True
            else:
                hash_map[total] = i

        return False