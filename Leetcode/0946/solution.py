class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j, stk = 0, []
        for item in pushed:
            stk.append(item)
            while stk and stk[-1] == popped[j]:
                stk.pop()
                j += 1
        return not stk