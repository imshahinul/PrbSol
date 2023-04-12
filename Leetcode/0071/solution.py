class Solution:
    def simplifyPath(self, path: sub) -> sub:
        stk = []

        for sub in path.split('/'):
            if sub in ('', '.'):
                continue
            if sub == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(sub)

        return '/' + '/'.join(stk)