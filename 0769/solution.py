class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunk_sz = 0
        max_elm = arr[0]
        for i in range(len(arr)):
            if max_elm < arr[i]:
                max_elm = arr[i]
            if max_elm == i:
                chunk_sz += 1
        return chunk_sz