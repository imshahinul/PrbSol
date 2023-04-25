class SmallestInfiniteSet:

    def __init__(self):
        self.pop_set = set()

    def popSmallest(self) -> int:
        i = 1
        while i in self.pop_set:
            i += 1
        self.pop_set.add(i)
        return i

    def addBack(self, num: int) -> None:
        self.pop_set.discard(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)