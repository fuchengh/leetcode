class RandomizedSet:

    def __init__(self):
        self.keys = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.keys)
        self.keys.append(val)
        return True

    def remove(self, val: int) -> bool:
        # move last element to this index
        if val in self.keys:
            idx = self.dict[val]
            last_elem = self.keys[-1]
            self.dict[last_elem] = idx
            self.keys[idx] = last_elem
            # delete duplicate items
            self.keys.pop()
            del self.dict[val]
            return True
        return False
    def getRandom(self) -> int:
        return choice(self.keys)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()