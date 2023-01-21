class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        out = []

        def valid_part(pt):
            if pt == '0' or (pt[0] != '0' and 0 < int(pt) < 256):
                return True

        for i in range(1, 4):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    if k >= len(s):
                        break
                    else:
                        x1, x2, x3, x4 = s[:i], s[i:j], s[j:k], s[k:]
                        if valid_part(x1) and valid_part(x2) and valid_part(x3) and valid_part(x4):
                            out.append("{0}.{1}.{2}.{3}".format(x1, x2, x3, x4))
        return out
