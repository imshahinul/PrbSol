class RandomizedSet:

    def __init__(self):
        self.s = []
        self.mapping = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.mapping:
            return False
        self.mapping[val] = len(self.s)
        self.s.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mapping:
            return False
        index = self.mapping[val]
        self.mapping[self.s[-1]] = index
        del self.mapping[val]
        self.s[index] = self.s[-1]
        self.s.pop()
        return True

    def getRandom(self) -> int:
        index = randint(0, len(self.s) - 1)
        return self.s[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()