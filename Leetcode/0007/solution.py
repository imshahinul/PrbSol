class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if len(s) == 1:
            return x
        if x > 0:
            out = int(str(x)[::-1])
        else:
            out = -1 * int(str(x)[1:][::-1])

        return 0 if out < -(2 ** 31) or out > 2 ** 31 else out