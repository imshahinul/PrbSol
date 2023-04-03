class Solution:
    def binary_search(self, nums, target):
        low = 0
        high = len(nums) - 1
        out = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= target:
                out = mid
                low = mid + 1
            else:
                high = mid - 1
        return out

    def create_prefix_sum(self, nums):
        prefix_sum = [0 for i in range(len(nums))]
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        return prefix_sum

    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        p_s = self.create_prefix_sum(nums)
        out = []
        for q in queries:
            idx = self.binary_search(nums, q)
            tt = len(nums) * q
            if idx == -1:
                no_of_op_s = p_s[len(nums) - 1] - (tt)
                out.append(no_of_op_s)

            else:
                sm = idx - 0 + 1
                plus_ops = (sm * q) - p_s[idx]
                bg = len(nums) - idx - 1
                minus_ops = (p_s[len(nums) - 1] - p_s[idx] - (bg * q))

                out.append(plus_ops + minus_ops)
        return out