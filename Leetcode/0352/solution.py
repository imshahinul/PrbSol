class SummaryRanges:

    def __init__(self):
        self.stream = []

    def addNum(self, value: int) -> None:
        if not self.stream:
            self.stream.append([value, value])
        else:
            temp = (None, -1)
            for i, it in enumerate(self.stream):
                if it[0] <= value <= it[1]:
                    temp = (None, 1)
                    break
                if value == it[0] - 1:
                    if temp[0] == None:
                        it[0] -= 1
                        temp = (it, i)
                    else:
                        pre = self.stream[temp[1]]
                        pre[1] = it[1]
                        self.stream.remove(it)
                        break
                elif value == it[1] + 1:
                    if temp[0] == None:
                        it[1] += 1
                        temp = (it, i)
                    else:
                        pre = self.stream[temp[1]]
                        pre[0] = it[0]
                        self.stream.remove(it)
                        break
            if temp[1] == -1:
                self.stream.append([value, value])

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.stream, key=lambda x: x[0])

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()