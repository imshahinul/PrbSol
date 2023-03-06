class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) >> 1
            if arr[mid] - mid - 1 >= k:
                high = mid
            else:
                low = mid + 1
        return arr[low - 1] + k - (arr[low - 1] - (low - 1) - 1)