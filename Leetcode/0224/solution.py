class Solution:
    def calculate(self, s: str) -> int:
        out = 0
        operands = 0
        operator = 1
        stack = [operator]

        for ch in s:
            if ch.isdigit():
                operands = operands * 10 + (ord(ch) - ord('0'))
            elif ch == '(':
                stack.append(operator)
            elif ch == ')':
                stack.pop()
            elif ch == '+' or ch == '-':
                out += operator * operands
                operator = (1 if ch == '+' else -1) * stack[-1]
                operands = 0

        return out + operator * operands