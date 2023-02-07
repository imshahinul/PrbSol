class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        out = []
        min_d = math.inf

        arr.sort()

        for i in range(len(arr) - 1):
            curr_diff = arr[i + 1] - arr[i]
            if curr_diff < min_d:
                min_d = curr_diff
                out = []
            if curr_diff == min_d:
                out.append([arr[i], arr[i + 1]])

        return out