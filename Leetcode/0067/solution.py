class Solution:
    def addBinary(self, a: str, b: str) -> str:
        mxl = max(len(a), len(b))
        a = a.zfill(mxl)
        b = b.zfill(mxl)
        out = ''
        cf = 0
        for i in range(mxl - 1, -1, -1):
            swp = cf
            if a[i] == '1':
                swp += 1
            if b[i] == '1':
                swp += 1

            if swp % 2 == 1:
                out = '1' + out
            else:
                out = '0' + out

            if swp < 2:
                cf = 0
            else:
                cf = 1

        if cf != 0:
            out = '1' + out
        return out