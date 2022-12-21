class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hash_map = {num: i for i, num in enumerate(nums)}

        c = 0
        for i, num in enumerate(nums):
            second_num = num + k
            if second_num in hash_map and hash_map[second_num] != i:
                c += 1
                del hash_map[second_num]
        return c