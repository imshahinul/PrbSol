class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def disrance(p):
            px, py = p
            return abs(px - rCenter) + abs(py - cCenter)
        return sorted([[i,j] for i in range(rows) for j in range(cols)], key=disrance)