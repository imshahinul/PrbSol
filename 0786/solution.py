class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        sorted_fraction = []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                sorted_fraction.append([arr[i] / arr[j], arr[i], arr[j]])

        sorted_fraction.sort(key=lambda x: x[0])

        return [sorted_fraction[k - 1][1], sorted_fraction[k - 1][2]]