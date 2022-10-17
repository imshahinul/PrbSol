class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        d_log = []
        l_log = []
        for log in logs:
            first_space_index = log.index(' ')
            if log[first_space_index + 1].isdigit():
                d_log.append(log)
            else:
                l_log.append((log[:first_space_index], log[first_space_index + 1:]))

        l_log.sort(key=lambda x: (x[1], x[0]))
        out = []
        for idn, letter in l_log:
            out.append(idn + ' ' + letter)

        return out + d_log