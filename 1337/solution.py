class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakest = []
        for i in range(len(mat)):
            weakest.append([mat[i].count(1), i])
        weakest.sort(key=lambda x: (x[0], x[1]))
        return [i for _, i in weakest[:k]]