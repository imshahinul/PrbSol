class Solution:
    def isValid(self, s: str) -> bool:
        ms = []
        for ch in s:
            if ch == '(':
                ms.append(')')
            elif ch == '{':
                ms.append('}')
            elif ch == '[':
                ms.append(']')
            elif not ms or ms.pop() != ch:
                return False
        return not ms