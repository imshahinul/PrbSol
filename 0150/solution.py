class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
        }

        for t in tokens:
            if t in ops:
                y = s.pop()
                x = s.pop()
                s.append(ops[t](x, y))
            else:
                s.append(int(t))

        return s[0]