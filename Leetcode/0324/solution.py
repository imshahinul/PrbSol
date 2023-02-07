class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        pow10s = [10 ** i for i in range(5)]
        buckets = [[] for i in range(10)]
        indices = []

        for i in range(len(nums) - 2 + (len(nums) % 2), -1, -2):
            indices.append(i)
        for i in range(len(nums) - 1 - (len(nums) % 2), 0, -2):
            indices.append(i)

        pow10 = 0
        nums_sorted = False
        while not nums_sorted:
            for i in indices:
                digit = (nums[i] // pow10s[pow10]) % 10
                buckets[digit].append(nums[i])

                if len(buckets[digit]) == len(nums):
                    nums_sorted = True
                    break
            j = 0
            for bucket in buckets:
                for num in bucket:
                    nums[indices[j]] = num
                    j += 1

            buckets = [[] for i in range(10)]
            pow10 += 1