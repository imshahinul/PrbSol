class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        sub = 2 * numRows - 2
        out = []
        for i in range(1, numRows + 1):
            diff = sub if i == numRows else 2 * numRows - 2 * i
            x = i - 1
            while x < len(s):
                out.append(s[x])
                x += diff
                diff = sub - diff
                if diff == 0:
                    diff = sub
        return ''.join(out)